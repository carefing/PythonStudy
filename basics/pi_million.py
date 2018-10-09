"""
read first million digits of pi from file
check whether your birthday appear in pi

使用 try-except 代码块来处理异常
"""

import re

def main():
    file = 'test_file/pi_first_million.txt'
    lines = []
    try:
        with open(file) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print('the file ' + file + ' does not exist.')
    except IOError:
        print('read file ' + file + ' error')

    pi_string = ''
    for line in lines:
        pi_string += line.strip().replace(' ', '')
    # print(pi_string[:100])

    # find birthday not contained in pi and save in file
    births = []
    for one in range(8, 9):
        for two in range(4, 6):
            for three in range(10):
                for four in range(10):
                    if not re.match(r'^[0][1-9]|[1][0-2]$', '' + str(three) + str(four)): # month regex
                        continue
                    for five in range(10):
                        for six in range(10):
                            if not re.match(r'^[0][1-9]|[1-2][0-9]|[3][0-1]$', '' + str(five) + str(six)): # day regex
                                continue
                            num = '' + str(one) + str(two) + str(three) + str(four) + str(five) + str(six)
                            if num not in pi_string:
                                # print(num + ' not in first million digits of PI!')
                                births.append(num)
    dst_file = 'test_file/not_in_pi.txt'
    try:
        with open(dst_file, 'w') as file_object:
            for birth in births:
                file_object.write(birth + '\n')
    except FileNotFoundError:
        print('the file ' + dst_file + ' does not exist.')
    except IOError:
        print('write file ' + dst_file + ' error')
    
    birthday = input('Enter your birthday, in the form yymmdd: ')
    if birthday in pi_string:
        print('Your birthday appears in the first million digits of PI!')
    else:
        print("Your birthday doesn't appear in the first million digits of PI.")


if __name__ == '__main__':
    main()