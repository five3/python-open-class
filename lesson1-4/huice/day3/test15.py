import sys
# ImportError:导入模块错误
# import A

# IndexError:索引超出范围
# list1 = [1,2,3]
# print list1[3]

# KeyError:字典中不存在的键
# dict1 = {'name':'ivy','age':20,'gender':'female'}
# print dict1['height']

# NameError：访问没有定义的变量
# print a

# IndentationError:缩进错误
# if 1==1:
# print 'aaa'

# SyntaxError:语法错误
# list2 = [1,2,3,4

# TypeError:不同类型间的无效操作
# print 1+'1'

# ZeroDivisionError:除数为0
# print 5/0

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')
