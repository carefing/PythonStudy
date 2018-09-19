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