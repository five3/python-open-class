

"""
    1、返回原对象
"""


def warp(obj):
    # TODO：something
    obj.name = 'python'

    return obj

@warp
class Bar(object):
    def __init__(self):
        pass

@warp
def foo():
    pass


"""
    2、返回包装的相似对象 - 普通函数装饰器、类方法装饰器、类装饰器
"""


def outer(obj):         # 函数装饰器
    def inner():
        obj()

    return inner

@outer
def zoo():  # foo = outer(zoo)
    pass


def outer2(obj):         # 类方法装饰器
    def inner(self):
        obj(self)

    return inner


class Zoo1(object):
    def __init__(self):
        pass

    @outer2
    def zoo(self):
        pass


def outer4(cls):         # 类装饰器
    class inner(object):
        def __init__(self):
            self.cls = cls()

        def __getattr__(self, attr):
            return getattr(self.cls, attr)

        def __setattr__(self, attr, value):
            return setattr(self.cls, attr, value)

    return inner


@outer4
class Zoo3(object):
    def __init__(self):
        pass

    def say(self):
        print('hello world!')


"""
    3、返回其它对象或数据
"""


class Prop(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        return self.fget(instance)


class Foo(object):
    def __init__(self, height, weigth):
        self.height = height
        self.weigth = weigth

    @Prop
    def ratio(self):
        return self.height / self.weigth

    @Prop
    def name(self):
        return 'Tom'


"""
    4、类实现的装饰器, 即用类模拟函数
"""


class Warp(object):
    def __init__(self):
        pass

    def __call__(self, obj):
        obj.name = 'warp'
        return obj


@Warp()
def foo2():
    pass


if '__main__' == __name__:
    # b = Bar()
    # print(b.name)
    # print(foo.name)
    # foo = Foo(176, 120)
    # print(foo.ratio)
    print(foo2.name)
    pass

