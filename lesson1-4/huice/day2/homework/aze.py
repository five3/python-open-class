a = '''uuuuuueqwoiej231aaaa8230912jdlskdasks22ddddddsdjasjdmnmxczfddfd56555555zmwqeoiqwoizcmmmmmm'''
b = list(a)
n = 1
max = 0
for i in range(len(b)):
    if i >= 1:
        if b[i] == b[i-1]:
            n += 1
        else:
            if max < n:
                max_str = []
                max_str.append(b[i - 1])
                max, n = n,1
            if max == n:
                max_str.append(b[i - 1])
                max, n = n, 1
            else:
                n = 1
    if i == len(b)-1 and max <= n:
        max = n
        max_str.append(b[i])
print(max,max_str)
for i in max_str:
    print(i*max)
