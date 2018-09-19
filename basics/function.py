from random import randint

def roll_dice(n = 2):
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total

def join_str(*strs):
    result = ''
    for str in strs:
        result += str
    return result

if __name__ == '__main__':
    print('roll 1 dice and get point:', roll_dice(1))
    print('roll 2 dices and get point:', roll_dice())
    print('roll 3 dices and get point:', roll_dice(3))
    print('join_str(\'hello\', \' world\'):', join_str('hello', ' world'))
    print('join_str(\'hello\', \' world\', \' - carefing\'):', join_str('hello', ' world', ' - carefing'))