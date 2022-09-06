import re
import pyperclip


class RegTransfer:
    def __init__(self, peripherals, text):
        self.peripherals = peripherals
        self.slice = False
        self.start = 0
        self.end = 0
        self.text = text
        self.dict = {}
        self.out = ''
        self.err = ''
        self.reserve_num = 0
        self.var_type = ' __IO uint32_t'
        self.reserve_name = 'RESERVED'
        self.struct_type = 'typedef struct\n{\n'

    def match_str(self):
        match_regex = re.compile(r'(' '\n'
                                 r'            (\#define)' '\n'
                                 r'            (\s+)' '\n'
                                 r'            (\w+)' '\n'
                                 r'            (\s+)' '\n'
                                 r'            (0[x][0-9a-f]+)' '\n'
                                 r'            (\n)?' '\n'
                                 r'            )', re.VERBOSE | re.IGNORECASE)

        for groups in match_regex.findall(self.text):
            value = groups[3]
            key = int(groups[5], 16)
            if key in self.dict.keys() or value in self.dict.values():
                self.err = '寄存器' + value + '名或地址重复'
                return False
            else:
                self.dict.update({key: value})

        return True

    def assert_offset(self):
        for i in self.dict.keys():
            if i % 4 != 0:
                self.err = '寄存器' + self.dict[i] + '的地址未4字节对齐'
                return False
            return True

    def gene_str(self):
        max_addr = max(self.dict.keys())
        all_reg = ''
        for i in range(0, max_addr + 4, 4):
            if i in self.dict.keys():
                reg_name = self.dict[i]
            else:
                self.reserve_num += 1
                reg_name = self.reserve_name + str(self.reserve_num)

            if self.slice:
                if self.start is None:
                    reg_name = reg_name[:self.end]
                elif self.end is None:
                    reg_name = reg_name[self.start:]
                else:
                    reg_name = reg_name[self.start:self.end]

            all_reg += self.var_type + ' ' + reg_name + ';\n'

        self.out = self.struct_type + all_reg + '} ' + self.peripherals

    def transfer(self):
        res = self.match_str()
        if not res:
            return False
        if not self.dict:
            self.err = '正则匹配失败'
            return False
        res = self.assert_offset()
        if not res:
            return False
        self.gene_str()
        return True


if __name__ == '__main__':
    name = 'SDIO_TypeDef'
    text = str(pyperclip.paste())
    reg = RegTransfer(name, text)
    result = reg.transfer()
    if result:
        print(reg.out)
        pyperclip.copy(reg.out)
    else:
        print(reg.err)
