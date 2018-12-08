from multiprocessing import Process, Pool
import os
import subprocess


subprocess.Popen(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
result = os.popen('dir')
print(type(result))
print(result.read())


def func(arg):
    print('arg:', arg)
    print('pid:', os.getpid())


p = Process(target=func, args=('test',))
print('Child process will start.')
p.start()
p.join()
print('Child process was end.')

# 使用线程池
p = Pool(4)
for i in range(5):
    p.apply_async(func, args=(i,))

p.close()
p.join()
