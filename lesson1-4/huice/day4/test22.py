import re

re.match('p', 'python')
re.match('p', 'www.python')

print(re.match(r'p', 'python'))
print(re.match(r'p', 'www.python'))
print(re.search(r'p', 'www.python'))


string = '23432werwre2342werwrew'
m = re.match(r'(\d*)([a-zA-Z]*)', string)


m = re.match(r'^(\d{3})-(\d{3,8})', '010-12345 AAAAA')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

print(re.findall(r'\d+', '102300789wd2200,6783w'))

result = 'a b   c'.split(' ')
print(result)

result = re.split(r'\s+', 'a b   c')
print(result)


