import re

'''
[a-zA-Z0-9]   匹配大小写字母与数字
[a-zA-Z]      匹配大小写字母
\@    a\@b     a@b   (字符转义)
\.    a\.b     a.b   (字符转义)
'''

def emails(e):
    if len(e)>= 5:
        if re.match(r"^[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",e) !=None:
            return '邮箱格式正确！'
    return '邮箱格式有误'


e = input("请输入email:")
print(e)
a = emails(e)
print(a)

