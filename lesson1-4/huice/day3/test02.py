
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print('-------------')

enroll('tianweifeng', 0)
enroll('liuze', 0, 7, 'Shanghai')
enroll(gender=1, age=5, name='zhangsan')


def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())


def enroll2(name, gender, *kw):
    print('name:', name)
    print('gender:', gender)
    for key in kw:
        print(key)
    print('-------------')

kw = [6, 'beijing', 'huahuayouzhiyuan']
enroll2('liuze', 1, kw[0], kw[1], kw[2])
enroll2('liuze', 1, *kw)
#
#
def enroll3(name, gender, **kw):
    print('name:', name)
    print('gender:', gender)
    for key,value in list(kw.items()):
        print(key+":"+str(value))
    print('-------------')

kw = {'age':7, 'city':'beijing', 'school':'huahuayouzhiyuan'}
enroll3('tianweifeng', 1, age=kw['age'], city=kw['city'], school=kw['school'])
enroll3('tianweifeng', 1, **kw)


