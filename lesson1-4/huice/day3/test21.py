import random

print(random.randint(0, 10))
print(random.random())
print(random.randrange(0, 10))
print(random.randrange(2, 12, 2))

array = [2, 3, 4, 5]
print(random.sample(array, 2))


# 1
import time
date_start = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time_start = time.mktime(date_start)

date_now = time.localtime()
time_now = time.mktime(date_now)

random_time = random.uniform(time_start, time_now)
result = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(random_time))
print(result)

# 2
result = {}
all = ['大王', '小王']
for x in ['红桃', '黑桃', '梅花', '方块']:
    for i in range(1, 14):
        all.append(x + str(i))

random.shuffle(all)
dipai = all[-3:]
all = all[:-3]

dizhu = all[::3] + dipai
nongmin1 = all[1::3]
nongmin2 = all[2::3]
result = {'地主':dizhu, '农民1':nongmin1, '农民2':nongmin2}

for key, value in list(result.items()):
    print(key + ':', end=' ')
    for pai in value:
        print(pai, end=' ')
    print('')