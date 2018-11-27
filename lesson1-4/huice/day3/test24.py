import re

def strings(url):
    listt = ['.php','.html','.asp','.jsp']
    for lis in listt:
        suffix = re.findall(lis, url)
        if len(suffix)>0:
            return lis


url = 'http://www.cnblogs.com/fnng/archive/2013/05/20/3089816.html'

a = strings(url)
print(a)