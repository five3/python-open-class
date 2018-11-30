import time

print(time.time())
print(time.ctime())
print(time.ctime(1))
print(time.asctime())
print(time.asctime([2017,10,13,13,29,18,4,286,0]))
print(time.mktime(time.localtime()))

# tuple_time可以不传，不传返回当前时间格式化后的结果
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%H:%M:%S %m/%d/%Y'))
print(time.strftime('%Y-%m-%d'))

# 获取一个小时前的时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-3600)))

print(time.strptime('2017-03-15 08:00:00', '%Y-%m-%d %H:%M:%S'))
print(time.strptime('17:27:33 03/18/2017', '%H:%M:%S %m/%d/%Y'))
