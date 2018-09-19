"""
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=false)
"""

print('Hello world!')
print('Hello', 'world', end='!\n')
print('Hello', 'world', sep=', ', end='!\n')

a = 123
b = 321
print('%d + %d = %d' % (a, b, a + b))

c = 3.14
print('c = %.3f' % c)