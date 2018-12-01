n = 0
def foo():
    m = 0
    n = 1
    print(locals())
    print(globals())

foo()
print(locals())
print(globals())
