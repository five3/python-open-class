def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

x = 50
func(x)
print('x is still', x)


def func2():
    global x
    print('x is',x)
    x = 2
    print('Changed local x to',x)

x =50
func2()
print('Value of x is ',x)

# import sys
# sys.setrecursionlimit(1500)
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print factorial(5)
# print factorial(1000)
#
# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
# print fact(1000)