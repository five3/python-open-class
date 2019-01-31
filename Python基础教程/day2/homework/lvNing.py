max = ""
max_times = 0
k = ""
refer = ""
n = 1
for i in s:
    if  i == refer:
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
