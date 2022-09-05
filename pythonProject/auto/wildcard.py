import re


# . 只匹配一个字符
def wildcard():
    atRegex = re.compile(r'.at')
    match_list = atRegex.findall('The cat in the hat sat on the flat mat')
    print(match_list)


# .*匹配所有字符
def match_all():
    nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    mo = nameRegex.search('First Name: Al Last Name: Sweigart')
    print(mo.group())
    print(mo.groups())
    print(mo.group(1))
    print(mo.group(2))


# 贪心匹配和非贪心匹配
def non_greedy_match_all():
    nongreedyRegex = re.compile(r'<.*?>')
    mo = nongreedyRegex.search('<To serve man> for dinner.>')
    print(mo.group())

    greedyRegex = re.compile(r'<.*>')
    mo = greedyRegex.search('<To serve man> for dinner.>')
    print(mo.group())


# 匹配换行符
def match_newline_with_dot():
    noNewLineRegex = re.compile('.*')
    mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.'
                               '\nUphold the law.').group()
    print(mo)

    newLineRegex = re.compile('.*', re.DOTALL)
    mo = newLineRegex.search('Serve the public trust.\nProtect the innocent.'
                             '\nUpload the law.').group()
    print(mo)


# 忽略大小写
def match_ignore_rescase():
    robocop = re.compile(r'robocop', re.IGNORECASE)

    mo = robocop.search('RoboCop is part man, part matchine, all cop').group()
    print(mo)

    mo = robocop.search('ROBOCOP protects the innocent.').group()
    print(mo)

    mo = robocop.search('Al, why does programming book talk about robocop so much?').group()
    print(mo)


def match_then_sub():
    namesRegex = re.compile(r'Agent \w+')
    mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
    print(mo)
    sub_str = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
    print(sub_str)

    agentNamesRegex = re.compile(r'Agent (\w)\w*')
    # \1 由分组1，即(\w)匹配的字符替代
    mo = agentNamesRegex.findall('Agent Alice told Agent Carol that Agent '
                                 'Eve knew Agent Bob was a double agent.')
    print(mo)
    sub_str = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent '
                                             'Eve knew Agent Bob was a double agent.')
    print(sub_str)


# 参数组合
def cmb_params():
    # 不区分大小写，使用dot匹配换行
    somRegxValue = re.compile('foo', re.IGNORECASE | re.DOTALL)


match_then_sub()
