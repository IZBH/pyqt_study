import re
from typing import Optional, Match


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# 正则匹配
def isPhoneNumber_re(text):
    phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    match: Optional[Match[str]] = phone_num_regex.search(text)
    return match


# 括号分组
def isPhoneBUmber_re_brackets(text):
    phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    match: Optional[Match[str]] = phone_num_regex.search(text)
    return match


# 括号分组+匹配括号
def isPhoneBUmber_re_match_brackets(text):
    phone_num_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
    match: Optional[Match[str]] = phone_num_regex.search(text)
    return match


# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))
mo = isPhoneBUmber_re_match_brackets('(415)-555-4242 is a phone number')
print(mo.groups())
print(mo.group())
print(mo.group(1))
print(mo.group(2))