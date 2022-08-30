from PIL import Image
import numpy as np
import os
from img_transfer import *


class transfer_img(object):
    def __init__(self):
        # resize
        self.resize = True
        self.resize_row = 100
        self.resize_col = 100
        # crop
        self.crop = True
        self.crop_list = [90, 80, 230, 160]
        # RGB565
        self.rgb565 = True
        # 输出格式
        self.out_h_file = True
        self.out_bin_file = True
        self.align_bin = True
        self.bin_size = 20*1024
        self.merge_bin = True
        # 路径
        self.path = ""
        self.f_name = ""
        self.arr_name = "img_arr"

    def transfer(self):
        path = self.path
        bin_path = ""
        if self.resize:
            path = resize_img(path, self.f_name, self.resize_row, self.resize_col)

        if self.crop:
            path = crop_img(path, self.f_name, self.crop_list)

        arr = img2arr(path)

        if self.rgb565:
            arr2rgb565(arr)

        if self.out_h_file:
            arr2H_file(arr, self.f_name, self.arr_name)

        if self.out_bin_file:
            bin_path = arr2bin(arr, self.f_name)

        if self.align_bin:
            align_bin(self.bin_size, bin_path)

