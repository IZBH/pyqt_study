import re
import pyperclip

str_variable_type = ' __IO uint32_t'
str_end = ';\n'
str_reserve = 'RESERVED'
str_struct_name = 'SDIO_TypeDef'
str_struct_start = 'typedef struct\n{\n'
str_struct_end = '} '


# 正则表达式匹配 #define开头 包含0x开头 换行结束的字符串
# 提取其中寄存器名和寄存器地址
def match_str(text):
    match_regex = re.compile(r'''(
        (\#define)
        (\s+)
        (\w+)
        (\s+)
        (0[x][0-9a-f]+)
        (\n)?
        )''', re.VERBOSE | re.IGNORECASE)

    offset_dict = {}
    for groups in match_regex.findall(text):
        value = groups[3]
        key = int(groups[5], 16)
        if key in offset_dict.keys() or value in offset_dict.values():
            return False
        else:
            tmp_dict = {key: value}
            offset_dict.update(tmp_dict)
    return offset_dict


# 检查地址偏移值
def assert_offset_dict(offset_dict):
    for i in offset_dict.keys():
        if i % 4 != 0:
            return False
        else:
            return True


# 生成字符串
def generate_str(offset_dict):
    max_offset = max(offset_dict.keys())
    map_str: str = ''
    reserve_num = 0
    for i in range(0, max_offset + 4, 4):
        if i in offset_dict.keys():
            reg_name = offset_dict[i]
        else:
            reserve_num += 1
            reg_name = str_reserve + str(reserve_num)
        map_str += str_variable_type + reg_name + str_end
    return str_struct_start + map_str + str_struct_end + str_struct_name + ';'


def_str = str(pyperclip.paste())

match_dict = match_str(def_str)
if not match_dict:
    print("寄存器名或地址重复")
tmp_str = generate_str(match_dict)
print(tmp_str)
