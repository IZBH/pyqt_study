import cv2
import numpy as np

import cv2
import numpy as np
from PIL import Image


def read_yuv422(yuv_arr, rows, cols):
    # 创建y分量
    img_y_1 = np.zeros((rows, int(cols / 2)), np.uint8)
    img_y_2 = np.zeros((rows, int(cols / 2)), np.uint8)
    img_y = np.zeros((rows, cols), np.uint8)

    # 创建u分量
    img_u = np.zeros((rows, int(cols / 2)), np.uint8)

    # 创建v分量
    img_v = np.zeros((rows, int(cols / 2)), np.uint8)

    # 读取内存中数据
    num = 0
    for i in range(rows):
        for j in range(int(cols / 2)):
            img_y_1[i, j] = yuv_arr[num]
            img_u[i, j] = yuv_arr[num + 1]
            img_y_2[i, j] = yuv_arr[num + 2]
            img_v[i, j] = yuv_arr[num + 3]
            num += 4

    for i in range(rows):
        for j in range(int(cols / 2)):
            img_y[i, 2 * j] = img_y_1[i, j]
            img_y[i, 2 * j + 1] = img_y_2[i, j]

    return img_y, img_u, img_v


# 把YUV格式数据转换为RGB格式
def yuv2rgb422(y, u, v):
    """
    :param y: y分量
    :param u: u分量
    :param v: v分量
    :return: rgb格式数据以及r,g,b分量
    """

    rows, cols = y.shape[:2]

    # 创建r,g,b分量
    r = np.zeros((rows, cols), np.uint8)
    g = np.zeros((rows, cols), np.uint8)
    b = np.zeros((rows, cols), np.uint8)

    for i in range(rows):
        for j in range(int(cols / 2)):
            r[i, 2 * j] = max(0, min(255, y[i, 2 * j] + 1.402 * (v[i, j] - 128)))
            g[i, 2 * j] = max(0, min(255, y[i, 2 * j] - 0.34414 * (u[i, j] - 128) - 0.71414 * (v[i, j] - 128)))
            b[i, 2 * j] = max(0, min(255, y[i, 2 * j] + 1.772 * (u[i, j] - 128)))

            r[i, 2 * j + 1] = max(0, min(255, y[i, 2 * j + 1] + 1.402 * (v[i, j] - 128)))
            g[i, 2 * j + 1] = max(0, min(255, y[i, 2 * j + 1] - 0.34414 * (u[i, j] - 128) - 0.71414 * (v[i, j] - 128)))
            b[i, 2 * j + 1] = max(0, min(255, y[i, 2 * j + 1] + 1.772 * (u[i, j] - 128)))

    rgb = cv2.merge([b, g, r])

    return rgb, r, g, b


with open('yuv.log') as f:
    f_str = f.read()
    str_list = f_str.split(', ')
    arr = [int(x, 16) for x in str_list]
    print(len(arr))
    img_yuv = read_yuv422(arr, 200, 180)
    img_rgb = yuv2rgb422(img_yuv[0], img_yuv[1], img_yuv[2])
    # cv2.imshow("RGB", img_rgb[0])
    img = Image.fromarray(img_rgb[0])
    img.save('./tmp.jpg')
    img.show()
