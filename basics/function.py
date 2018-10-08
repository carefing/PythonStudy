"""
function practice

传递实参：
- 位置实参
- 关键字实参(可提供默认值，让实参变成可选)
- 传递列表(会实际修改列表，若不想修改，则传递列表的副本-切片)
- 传递任意数量的实参(*形参名)
- 传递任意数量的关键字实参(**形参名)

函数编写指南：
1. 应给函数指定描述性名称，且只在其中使用小写字母和下划线
2. 每个函数都应包含简要地阐述其功能的注释，注释紧跟在函数定义后面
3. 给形参指定默认值时，等号两边不要有空格，关键字实参也是如此
4. 形参很多，函数定义过长，则分行罗列，参数缩进2个tab，从而将参数列表和函数体区分开
5. 如果程序或模块中包含多个函数，可以用两个空行将相邻的函数分开

"""

from random import randint

def roll_dice(n=2):
    """roll n dices and get total points"""
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total


def join_str(*strs):
    """join strings"""
    result = ''
    for str in strs:
        result += str
    return result


def make_sandwich(*fillings):
    """describe sandwich with fillings"""
    print("\nMake a sandwich with the following fillings:")
    for filling in fillings:
        print('- ' + filling)


def build_profile(last, first, **info):
    """build user profile"""
    profile = {}
    profile['last_name'] = last
    profile['first_name'] = first
    for key, value in info.items():
        profile[key] = value
    return profile


if __name__ == '__main__':
    print('roll 1 dice and get point:', roll_dice(1))
    print('roll 2 dices and get point:', roll_dice())
    print('roll 3 dices and get point:', roll_dice(3))
    print('join_str(\'hello\', \' world\'):', join_str('hello', ' world'))
    print('join_str(\'hello\', \' world\', \' - carefing\'):', join_str('hello', ' world', ' - carefing'))
    make_sandwich('lettuce', 'egg')
    make_sandwich('lettuce', 'egg', 'ham')
    print('\nbuild a user profile:', build_profile('Zhu', 'Carefing', Gender='Female', Interest='Reading', Job='SW Engineer'))