"""
string:
"""

str1 = 'hello world!'
print('字符串:', str1, '的长度:', len(str1))
print('单词首字母大写:', str1.title())
print('字符串变大写:', str1.upper())
str1_upper = str1.upper()
print('字符串变小写:', str1_upper.lower())
print('字符串是不是写:', str1.isupper())
print('字符串是不是以hello开头:', str1.startswith('hello'))
print('字符串是不是以world结尾:', str1.startswith('world'))
str2 = '- Carefing'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
# 下标及字符串切片
str4 = 'abc123456'
print(str4[2])      # c
print(str4[2:])     # c123456
print(str4[:5])     # abc12
print(str4[2:5])    # c12 (not contain 3)
print(str4[::2])    # ac246
print(str4[3::2])   # 135
print(str4[::-1])   # 654321cba
print(str4[-3:-1])  # 45
print(str4[5:2:-1]) # 321