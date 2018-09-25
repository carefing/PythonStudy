"""
"""

import re

def check_qq():
    # qq is 5-12 digits
    qq = input('Please input QQ: ')
    match = re.match(r'^[1-9]\d{4,11}$', qq) # None or object
    if not match:
        print('QQ pattern is not correct.')
    else:
        print('QQ pattern is correct.')

def split_poem():
    poem = '春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。'
    setence = re.split(r'[,.，。]', poem)
    # print(setence) # ['春眠不觉晓', '处处闻啼鸟', '夜来风雨声', '花落知多少', '']
    while '' in setence:
        setence.remove('')
    print(setence) # ['春眠不觉晓', '处处闻啼鸟', '夜来风雨声', '花落知多少']

def purify_setence():
    setence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub(r'[操肏艹草曹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', setence, flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    print('Let\'s practice some regex!')
    print('Example 1: check qq account:')
    check_qq()
    print('------------------------------')
    print('Example 2: split poem:')
    split_poem()
    print('------------------------------')
    print('Example 3: purify setence:')
    purify_setence()
