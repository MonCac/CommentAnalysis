'''
用户名的规则：只能是大小写字母或数字，且不能以数字开头，长度为5~12位
'''
import re  ##引用内置正则表达式模块


def check_user(username):  # 定义个函数，备用个参数username
    pattern = "^[a-zA-Z][0-9a-zA-Z]{4,11}$"
    ##上面定义正则规则，下面正则固定写法re.match，规则在先字符串在后，储存在res变量中，全拼result；结果
    res = re.match(pattern=pattern, string=username)
    if res:  # 这里if判断如果值出来个给返回True反之False
        return True
    else:
        # print("用户名只能是大小写字母或数字，且不能以数字开头，长度为5~12位")
        return False
    # re.match:匹配成功返回一个match对象：<re.Match object; span=(0, 5), match='lency'>


'''
密码的规则：密码必须且只能由大小写字母和数字组成，长度为6~15位
print(ord(st)) #a-97 z-122 A-65 Z=90 0-48 9-57 将字符转换成ASCII
print(chr(97)) #将ASCII值转换成对应的字符
'''


def check_pwd(pwd):
    low = 0
    up = 0
    num = 0
    if len(pwd) >= 6 and len(pwd) < 15:
        # 原生比较/ASII数值比较
        for p in pwd:
            ##这里可参照ascii表来查明意义
            if ord(p) >= 97 and ord(p) <= 122:
                # print('小写字母')
                low += 1
            elif ord(p) >= 65 and ord(p) <= 90:
                # print('大写字母')
                up += 1
            elif ord(p) >= 48 and ord(p) <= 57:
                # print('数字')
                num += 1
            else:
                return False
    # 这里if判断，他们都通过了这些要求就给他们加1，如果最后的结果他们这几个条件都有1，则给它通过返回True
    # print(low,up,num)
    if up >= 1 or low >= 1 or num >= 1:
        return True
    else:
        # print("密码必须且只能由大小写字母和数字组成，长度为6~15位：")
        # main.select()
        return False

##整体思路，就是将他们成功返回True，失败则返回False，这些有用，后面会使用到这些返回值。
