s = "asdasj678596knxcn2132930knsdns12398mnfsdh234898ncmdnsdkj"
# 取出给定字符串中的数字，并打印出是偶数的字符，当打印次数大于10时退出

s = '''ueqwoiej231aaaa8230912jdlskdasks22dddddddsdjasjdmnmxczfdd5555fd565555555555zm555wqeoiqwoizcm'''
# 找出连续重复字符次数最多的子字符串
max_k = None
max_v = 0
save_ch = None
temp_ch = None
for ch in s:
    if temp_ch is None:
        save_ch = ch
        temp_ch = ch
        continue

    if temp_ch == ch:
        save_ch += ch
    else:
        if len(save_ch) > max_v:
            max_v = len(save_ch)
            max_k = save_ch
        save_ch = ch
        temp_ch = ch


print(max_k, max_v)

# 给定一个字母，找出其出现的次数
print(s.count('f'))
count = 0
for ch in s:
    if ch == 'f':
        count += 1
print(count)


max = ""
max_times = 0
k = ""
refer = ""
n = 1
for i in s:
    if i == refer:
        k = k + i
        n += 1
    else:
        if n > max_times:
            max = k
            max_times = n
            refer = i
            k = ""
            n = 1
        else:
            refer = i
            k = i
            n = 1
print(max, max_times)
