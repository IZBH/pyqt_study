from heapq import heappush
from turtle import width
from PIL import Image
import numpy as np
import os
import cv2

# row = 320
# col = 240

row = 100
col = 100


def resize_img(img_path, filename):
    img = Image.open(img_path)
    resize_img = img.resize((row, col), Image.Resampling.LANCZOS)
    if not os.path.exists("resize"):
        os.mkdir("resize")
    resize_path = './resize/%s.jpg' %filename
    resize_img.save(resize_path)
    return resize_path

def crop_img(img_path, filename):
    img = Image.open(img_path)
    crop_list = [90, 80, 230, 100]
    crop_img = img.crop(crop_list)
    if not os.path.exists("crop"):
        os.mkdir("crop")
    crop_path = './crop/%s.jpg' %filename
    crop_img.save(crop_path)
    return crop_path

def img2rgb565(img_path):
    img = np.array(Image.open(img_path))
    width = img.shape[1]
    height = img.shape[0]
    threshold = 0
    rgb565 = np.zeros((height, width), dtype=np.uint16)

    for i in range(0, height):
        for j in range(0, width):
            # if(img[i, j, 0] <= threshold) and (img[i, j, 1] <= threshold) and (img[i, j, 2] <= threshold):
            #     img[i, j, 0] = 0
            #     img[i, j, 1] = 0
            #     img[i, j, 2] = 0
            # rgb565[i, j] = ((int(img[i,j,0]) & 0xF8) << 8) | ((int(img[i,j,1]) & 0xFC) << 3) | (int(img[i,j,2]) >> 3)
            r = img[i, j][0] >> 3
            g = img[i, j][1] >> 2
            b = img[i, j][2] >> 3
            rgb565[i, j] = (r << 11) | (g << 5) | b

    return rgb565

def show_rgb565(rgb565, filename):
    width = rgb565.shape[1]
    height = rgb565.shape[0]
    rgb888 = np.zeros([height, width, 3], dtype=np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            r = ((rgb565[i, j] >> 11) & 0x1f) << 3
            g = ((rgb565[i, j] >>  5) & 0x3f) << 2
            b = (rgb565[i, j]         & 0x1f) << 3
            rgb888[i, j] = r, g, b
    img = Image.fromarray(rgb888)
    if not os.path.exists("show"):
        os.mkdir("show")
    show_path = './show/%s.jpg' %filename
    img.save(show_path)

def arr2Hfile(arr, filename):
    width = arr.shape[1]
    height = arr.shape[0]
    enterCount = 0
    cString = "#define imgWidth %d\n#define imgHeight %d\n\nconst uint8_t imgArray_%s[] = {\n"%(width, height, filename)
    for i in range(0, height):
        for j in range(0, width):

    
            cur_rgb565_l = arr[i, j] & 0xFF
            cur_rgb565_h = arr[i, j] >> 8
            rgb565Temp = "{:#04X}".format(cur_rgb565_h) + ", " + "{:#04X}".format(cur_rgb565_l)
            # rgb565Temp = "{:#06X}".format(arr[i, j])


            cString += rgb565Temp
            cString += ", "
            if(enterCount%16 == 15):
                cString += "\n"
            enterCount = enterCount + 1
    cString += "};"

    if not os.path.exists("h-file"):
        os.mkdir("h-file")
    c_head_path = './h-file/%s.h' %filename
    with open(c_head_path, 'w') as f:
        f.write(cString)
    return c_head_path

def arr2bin(arr, filename):
    if not os.path.exists("binfile"):
        os.mkdir("binfile")
    bin_path = './binfile/%s.bin' %filename
    arr_big_endian = np.asarray(arr, dtype = '>u2')
    arr_big_endian.tofile(bin_path)
    # arr_little_endian = np.asarray(arr, dtype=np.uint16)
    # arr_little_endian.tofile(bin_path)
    return bin_path

def align_bin(t_size, filename):
    with open(filename, "ab+") as f:
        size = f.tell()
        a_size = t_size - size
        data = np.zeros(a_size, dtype=np.uint8)
        f.write(data)
        size = f.tell()
        f.close()
    

def img_transfer(img_path, filename):
    resize_img_path = resize_img(img_path, filename)
    crop_path = crop_img(resize_img_path, filename)
    rgb565 = img2rgb565(img_path)
    show_rgb565(rgb565, filename)
    arr2Hfile(rgb565, filename)
    bin_path = arr2bin(rgb565, filename)
    # align_bin(20*1024, bin_path)
    # merge_bin("img_set.bin", bin_path)
    return bin_path

def dir_transfer(dir_path):
    i = 0
    for filename in os.listdir(dir_path):
        img_path = dir_path + '/' +filename
        bin_path = img_transfer(img_path, str(i))

        # if i % 4 == 0:
        #     merge_bin("quarter.bin", bin_path)
        i = i + 1
    print("all image transfer finished!")

def merge_bin(target, src):
    f_taget = open(target, "ab+")
    f_src = open(src, "rb")

    data = f_src.read()
    f_taget.write(data)
    f_taget.close()


# dir_transfer('./todo')
# with open("quarter.bin",  "ab+") as f:
#     size = f.tell()
#     print(size)
#     f.close()
img_transfer('HardwareLogo_Blue 2_00000.jpg', '20220823')