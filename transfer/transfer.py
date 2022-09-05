from PIL import Image
import numpy as np
import cv2
import os
 

def img2c_head(img_path, filename):
    img = np.array(Image.open(img_path))
    width = img.shape[1]
    height = img.shape[0]
    enterCount = 0
    threshold = 100
    cString = "#define imgWidth %d\n#define imgHeight %d\n\nconst unsigned short imgArray%d[] = {\n"%(width, height, int(filename))
    imgTest = np.zeros((height, width), np.uint16)
    for i in range(0, height):
        for j in range(0, width):
            
            if (img[i, j, 0] < threshold) and (img[i, j, 1] < threshold) and (img[i, j, 2] < threshold):
                img[i, j, 0] = 0
                img[i, j, 1] = 0
                img[i, j, 2] = 0

            cur_rgb565 = ((int(img[i,j,0]) & 0xF8) << 8) | ((int(img[i,j,1]) & 0xFC) << 3) | (int(img[i,j,2]) >> 3)
            rgb565Temp = "{:#06X}".format(cur_rgb565)
            imgTest[i, j] = cur_rgb565
            cString += rgb565Temp
            cString += ", "
            if(enterCount%16 == 15):
                cString += "\n"
            enterCount = enterCount + 1
    cString += "};"
    
    if not os.path.exists("output"):
        os.mkdir("output")
    c_head_path = './output/%s.h' %filename
    with open(c_head_path,'w') as f:
        f.write(cString)
    return imgTest

def data2bin(imgTest, filename):
    if not os.path.exists("binfile"):
        os.mkdir("binfile")
    bin_name = './binfile/%s.bin' %filename
    imgTest.tofile(bin_name)


def resize_img(img_path, filename):
    img = Image.open(img_path)
    new_img = img.resize((320, 240), Image.Resampling.LANCZOS)
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    new_img_path = './tmp/%s.jpg' %filename
    new_img.save(new_img_path)
    return new_img_path

def img_transfer(img_path, num):
    cpath = resize_img(img_path, num)
    data = img2c_head(cpath, num)
    data2bin(data, num)

def dir_transfer(dir_path):
    i = 0
    for filename in os.listdir(dir_path):
        img_path = dir_path + '/' + filename
        img_transfer(img_path, str(i))
        i = i + 1
    print("all image transfer finished!")

# dir_transfer('./HardwareLogo_Blue 2')
img_transfer('./HardwareLogo_Blue 2/HardwareLogo_Blue 2_00087.jpg', '9')


