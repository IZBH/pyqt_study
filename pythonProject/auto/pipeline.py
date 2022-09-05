import re


# 管道匹配多个分组
def match_pipeline():
    heroRegex = re.compile(r'Batman|Tina Fey')

    mo1 = heroRegex.search('Batman and Tiny Fey.')
    print(mo1.group())

    mo2 = heroRegex.search('Tiny Fey and Batman.')
    print(mo2.group())

    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = batRegex.search('Batmobile lost a wheel')
    print(mo.group())
    print(mo.group(1))


# 问号实现可选匹配
def question_mark_match():
    # wo 可出现0-1次
    batRegex = re.compile(r'Bat(wo)?man')

    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())

    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())


# 用星号匹配零次或多次
def Asterisk_match():
    # wo 可出现0-无穷次
    batRegex = re.compile(r'Bat(wo)*man')

    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())

    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())

    mo3 = batRegex.search('The Adventures of Batwowowowowowowowoman')
    print(mo3.group())


# 用加号匹配一次或多次
def plus_match():
    # wo 可出现1-无穷次
    batRegex = re.compile(r'Bat(wo)+man')

    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1)

    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())

    mo3 = batRegex.search('The Adventures of Batwowowowowowowowoman')
    print(mo3.group())


# 用花括号匹配特定次数
def curly_braces_match():
    # ha 出现3次
    haRegex = re.compile(r'(Ha){3}')
    mo1 = haRegex.search('HaHaHa')
    print(mo1.group())

    mo2 = haRegex.search('Ha')
    print(mo2)


# 贪心匹配
def greedy_match():
    greedyHaRegex = re.compile(r'(Ha){3,5}')
    mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
    print(mo1.group())


# 非贪心匹配
def none_greedy_match():
    none_reedyHaRegex = re.compile(r'(Ha){3,5}?')
    mo2 = none_reedyHaRegex.search('HaHaHaHaHaHa')
    print(mo2.group())


def find_all_match():
    # 不分组
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

    mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
    print(mo.group())

    match_list = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(match_list)

    # 分组
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

    mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
    print(mo.group())

    match_list = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(match_list)


# 字符分类
# \d    0-9的任何数字
# \D    除0-9数字以外的任何字符
# \w    任何字母，数字，下划线
# \W    除字母，数字，下划线以外的任何字符
# \s    空格，制表符，换行符
# \S    除空格，制表符，换行符以外的任何字符

# 字符匹配
def mas_match():
    xmasRegex = re.compile(r'\d+\s\w+')
    match_list = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, '
                                   '4 birds, 3 hens, 2 doves, 1 partridge')
    print(match_list)


# 建立自己的字符分类
def vowel_match():
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    match_list = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(match_list)

    consonantRegex = re.compile(r'[^aeiouAEIOU]')
    match_list = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(match_list)


# 16进制匹配
def hex_match():
    hexRegex = re.compile(r'0[xX][a-fA-F\d]{2}[,\s]?')
    match_list = hexRegex.findall('0X15, 0XAA, 0X1F, 0X'
                                  'C1, 0Xaa, 0X1f, 0Xc1, '
                                  '0x15, 0xAA, 0x1F, 0xC1, 0xAA, 0x1f, 0xc1, '
                                  'x0ff, b9aa, 0x1fa, 0XAF1, 0xzo, 0xbb')

    print(match_list)
    arr = [int(x[0:4], 16) for x in match_list]
    print(arr)

    hexRegex = re.compile(r'0x[a-f\d]{2}[,\s]?', re.IGNORECASE)
    match_list = hexRegex.findall('0X15, 0XAA, 0X1F, 0X'
                                  'C1, 0Xaa, 0X1f, 0Xc1, '
                                  '0x15, 0xAA, 0x1F, 0xC1, 0xAA, 0x1f, 0xc1, '
                                  'x0ff, b9aa, 0x1fa, 0XAF1, 0xzo, 0xbb')

    print(match_list)
    arr = [int(x[0:4], 16) for x in match_list]
    print(arr)


def insert_dollar_match():
    # 以hello开始的字符串
    beginsWithHello = re.compile(r'^Hello')
    mo = beginsWithHello.search('Hello world!')
    print(mo)
    mo = beginsWithHello.search('He said hello.')
    print(mo)

    # 匹配以数字0-9结束的字符串
    endsWithNumber = re.compile(r'\d$')
    mo = endsWithNumber.search('Your number is 42')
    print(mo)
    mo = endsWithNumber.search('Your number is forty two.')
    print(mo)

    # 匹配从开始到结束都是数字的字符串
    wholeStringIsNum = re.compile(r'^\d+$')
    mo = wholeStringIsNum.search('1234567890')
    print(mo)
    mo = wholeStringIsNum.search('12345xyz67890')
    print(mo)
    mo = wholeStringIsNum.search('12 34567890')
    print(mo)

    # 以数字开头，abc结尾的任意字符串，不包含\n\r
    endWithNumber = re.compile(r'^[0-9].*?abc$')
    mo = endWithNumber.search('123dabc')
    print(mo)


hex_match()
