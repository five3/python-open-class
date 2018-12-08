import os

# 查看和修改环境变量
print(os.environ)
os.environ['PYTHONIOENCODING'] = 'UFT-8'
print(os.environ)

# 执行命令
print(os.system('dir'))
os.system(r'C:\"Program Files (x86)\Mozilla Firefox\firefox.exe"')
os.startfile(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

# 目录文件操作
print(os.getcwd())      # 获取当前执行目录
print(os.listdir('.'))  # 列出当前目录内容，同于 dir
os.mkdir('D:\\test')    # 创建目录
os.makedirs('D:\\test\class01\stu01')   # 创建目录树
os.rmdir('D:\\test')    # 删除目录
os.removedirs('D:\\test\\1')        # 删除目录树

print(os.path.isfile('D:\\test\\class01\\stu01'))
print(os.path.isdir('D:\\test\\class01\\stu01'))
print(os.path.exists('D:\\test\\class01\\stu01'))
print(os.path.exists('D:\\test\\class01\\stu01\\1.doc'))
print(os.path.split('D:\\test\\class01\\stu01\\1.doc'))
print(os.path.join('D:\\git', 'python-open-class'))

print(os.path.abspath('.'))
os.chdir('D:\\')    # 同于cd命令
print(os.path.abspath('.'))


import shutil
shutil.copyfile('D:\\report\\20171009235827.html', 'D:\\1.html')
shutil.copy('D:\\report\\20171009235827.html', 'D:\\1.html')
shutil.copytree('D:\\report', 'D:\\report_temp')
shutil.copytree('D:\\report', 'D:\\report_temp', ignore=shutil.ignore_patterns('*.html'))
shutil.rmtree('D:\\report_temp')


#2 实现目录递归遍历，查找以.py结尾的文件，并将文件绝对路径存入log.txt文件。
res = []
def go_through(dir):
    # 遍历文件夹中的所有文件夹和文件
    for i in os.listdir(dir):
        # 判断是否是文件夹，如果是文件夹，就进行递归调用
        if os.path.isdir(dir + os.sep + i):
            go_through(dir + os.sep + i)
        else:
            # 如果是文件，判断最后是不是以.py结尾
            if i[-3:] == '.py':
                res.append(dir + os.sep + i)
go_through('D:\\test')
print(res)
