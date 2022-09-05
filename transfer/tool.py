from PIL import Image
import numpy as np
import os

def data2hexstr(array):
    str = ''
    for i in array:
        str += '0x{:02X}'.format(i) + ','
    str = str[:-1]
    return str

def array2rgb(array):
    tmp = np.array(array)
    tmp = tmp.reshape(3, 1024)
    arrayrgb = tmp.flatten('F')
    return arrayrgb

def rgb_info(array):
    head = array[0]
    data = array2rgb(array[1:])
    arr = np.hstack((head,data))
    return arr

# def arr2img(array):


def file_split(fname, size):
    f_array = np.fromfile(fname, dtype=np.uint8)
    array = f_array.reshape(f_array.size // size, size)

    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    
    for i in range(f_array.size // size):
        with open('./tmp/split%d.txt'% i,'w+') as tmp:
            info = rgb_info(array[i])
            str = data2hexstr(info)
            tmp.write(str)
    print("Done")








if __name__ == "__main__":
    file_split("test_batch.bin", 3073)






