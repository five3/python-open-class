def a(s):
    return 10 / int(s)

# def a(s):
#     if int(s) == 0:
#         raise ArithmeticError ('除数为0')
#     return 10 / int(s)


def b(s):
    return a(s) * 2

def c():
    b('0')


c()