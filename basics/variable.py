"""
Python variable type: str, int, float, complex, bool
"""

a = 12
b = 1000000000000000000000000000
c = 12.34
d = 13 + 5j
e = 'a'
f = 'Hello world!'
g = True

"""
Following output:

a = 12 then type(a) = <class 'int'>
b = 1000000000000000000000000000 then type(b) = <class 'int'>
c = 12.34 then type(c) = <class 'float'>
d = 13 + 5j then type(d) = <class 'complex'>
e = 'a' then type(e) = <class 'str'>
f = 'Hello world!' then type(f) = <class 'str'>
g = True then type(g) = <class 'bool'>
"""
print('a = 12 then type(a) =', type(a))
print('b = 1000000000000000000000000000 then type(b) =', type(b))
print('c = 12.34 then type(c) =', type(c))
print('d = 13 + 5j then type(d) =', type(d))
print('e = \'a\' then type(e) =', type(e))
print('f = \'Hello world!\' then type(f) =', type(f))
print('g = True then type(g) =', type(g))

"""
Following output example:

input string a: Hello world!
Hello world!
type(a) = <class 'str'>
input integer b: 34
34
type(b) = <class 'int'>
input float c: 45.678
45.678
type(c) = <class 'float'>
input complex d: 1+2j
(1+2j)
type(d) = <class 'complex'>
input bool e: False
True
type(e) = <class 'bool'>
"""
a = input('input string a: ')
print(a)
print('type(a) =', type(a))
b = int(input('input integer b: '))
print(b)
print('type(b) =', type(b))
c = float(input('input float c: '))
print(c)
print('type(c) =', type(c))
d = complex(input('input complex d: '))
print(d)
print('type(d) =', type(d))
e = bool(input('input bool e: '))
print(e)
print('type(e) =', type(e))