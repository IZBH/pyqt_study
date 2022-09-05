#! python3
# 读取剪贴板，找到电话号码和E-mail地址，替换掉剪贴板中的文本

import re
import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # 区号: 可选?;3位数字\d{3};括号括起来三位数字\(\d{3}\);或 |
    (\s|-|\.)?                          # 分隔符：可选?;空格\s;短横-;dot\.;或 |
    (\d{3})                             # 前3位: 3位数字 \d{3}
    (\s|-|\.)                           # 分隔符：同上
    (\d{4})                             # 后4位：同上
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # 扩展：可选?;任意数目的空格\s*;ext或x或ext.;2-5位数字\d{2-5}
    )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # 用户名：1个或多个字符+;字符可为小写字母，大写字母，数字，dot，下划线，百分号，加号，短横
    @                                   # @
    [a-zA-Z0-9.-]+                      # 域名:字母，数字，dot，短横
    (\.[a-zA-Z]{2,4})                   # 域名：dot+2-4个大小写字母\.[a-zA-Z]{2,4}   
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found')

# def test():
#     str_re = '400-822-9999   x  123'
#     m = phoneRegex.findall(str_re)
#     print(m)


