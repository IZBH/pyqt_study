from PIL import Image
import numpy as np
import os


def resize_img(img_path, filename, row, col):
    with Image.open(img_path) as img:
        new_img = img.resize((row, col), Image.Resampling.LANCZOS)
        if not os.path.exists("resize"):
            os.mkdir("resize")
        resize_path = './resize/%s.jpg' % filename
        new_img.save(resize_path)
        return resize_path


def crop_img(img_path, filename, crop_list):
    with Image.open(img_path) as img:
        new_img = img.crop(crop_list)
        if not os.path.exists("crop"):
            os.mkdir("crop")
        crop_path = './crop/%s.jpg' % filename
        new_img.save(crop_path)
        return crop_path


def img2arr(img_path):
    with Image.open(img_path) as img:
        arr = np.array(img)
        return arr


def arr2rgb565(arr):
    width = arr.shape[1]
    height = arr.shape[0]
    rgb565 = np.zeros((height, width), dtype=np.uint16)
    for i in range(0, height):
        for j in range(0, width):
            r = arr[i, j][0] >> 3
            g = arr[i, j][1] >> 2
            b = arr[i, j][2] >> 3
            rgb565[i, j] = (r << 11) | (g << 5) | b

    return rgb565


def rgb5652img(rgb565, filename):
    width = rgb565.shape[1]
    height = rgb565.shape[0]
    rgb888 = np.zeros([height, width, 3], dtype=np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            r = ((rgb565[i, j] >> 11) & 0x1f) << 3
            g = ((rgb565[i, j] >> 5) & 0x3f) << 2
            b = (rgb565[i, j] & 0x1f) << 3
            rgb888[i, j] = r, g, b
    img = Image.fromarray(rgb888)
    if not os.path.exists("show"):
        os.mkdir("show")
    show_path = './show/%s.jpg' % filename
    img.save(show_path)


def arr2H_file(arr, filename, arr_name):
    width = arr.shape[1]
    height = arr.shape[0]
    count = 0
    c_string = "#define img_width %d\n#define img_height %d\n\nconst uint8_t %s = {\n" % (
        width, height, arr_name
    )

    for i in range(0, height):
        for j in range(0, width):
            arr_l = arr[i, j] & 0xFF
            arr_h = arr[i, j] >> 8
            arr_str = "{:#04X}".format(arr_h) + ", " + "{:#04X}".format(arr_l)
            c_string += arr_str
            c_string += ", "
            if count % 16 == 15:
                c_string += "\n"
            count += 1
    c_string += "};"

    if not os.path.exists("H_file"):
        os.mkdir("H_file")
    c_head_path = './h-file/%s.h' % filename
    with open(c_head_path, 'w') as f:
        f.write(c_string)
    return c_head_path


def arr2bin(arr, filename):
    if not os.path.exists("bin_file"):
        os.mkdir("bin_file")
    bin_path = './bin_file/%s.bin' % filename
    arr_big_endian = np.asarray(arr, dtype='>u2')
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


def merge_bin(target, src):
    f_target = open(target, "ab+")
    f_src = open(src, "rb")

    data = f_src.read()
    f_target.write(data)
    f_target.close()
