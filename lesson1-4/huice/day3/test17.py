
def sub(a, b):
    if a < b:
        raise ArithmeticError('被减数不能小于减数')
    return a-b

# print sub(0,2)

# 2
a = input('请输入第一个数字')
b = input('请输入第二个数字')
try:
    a, b = int(a), int(b)
except ValueError:
    a = b = 0

print(a+b)


# 3
class IllegalNameError(NameError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str('用户名[%s]长度少于6位' % self.value)

class UserService(object):

    def register(self, name):
        if len(name)< 6:
            raise IllegalNameError(name)
        print("注册成功，欢迎[%s]" % name)

try:
    name = input('请输入用户名:')
    UserService().register(name)
except IllegalNameError as e:
    print(e)
