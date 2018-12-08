import threading
import threadpool
import time


def func(arg):
    print('arg:', arg)
    print('tid:', threading.get_ident())


for i in range(4):
    # 第一种方法
    t = threading.Thread(target=func, args=(i,))
    t.start()
    t.join()


# 第二种方法
class MyThread(threading.Thread):
    def __init__(self, arg):
        super().__init__()
        self.arg=arg

    def run(self):
        time.sleep(1)
        print('the arg is:%s' % self.arg)


tl = [MyThread(i) for i in range(4)]
[t.start() for t in tl]
[t.join() for t in tl]


# 线程池
name_list = ['huice', 'aa', 'bb', 'cc']
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(func, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()
