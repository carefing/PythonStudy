"""
掷骰子
"""

from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳支舞'
elif face == 3:
    result = '俯卧撑'
elif face == 4:
    result = '讲笑话'
elif face == 5:
    result = '学狗叫'
else:
    result = '做鬼脸'
print(result)