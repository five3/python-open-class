# import os

# print os.environ
# os.environ['PYTHONIOENCODING'] = 'UFT-8'
# print os.environ
#
# print os.system('dir')
# os.system(r'C:\"Program Files (x86)\Mozilla Firefox\firefox.exe"')
#
# os.startfile(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#
# import subprocess
# subprocess.Popen(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#
# result = os.popen('dir')
# print type(result)
# print result.read()

# print os.getcwd()
# print os.listdir('.')
# os.mkdir('D:\\test')
# os.makedirs('D:\\test\class01\stu01')
# os.rmdir('D:\\test')
# os.removedirs('D:\\test\\1')

# print os.path.isfile('D:\\test\\class01\\stu01')
# print os.path.isdir('D:\\test\\class01\\stu01')
# print os.path.exists('D:\\test\\class01\\stu01')
# print os.path.exists('D:\\test\\class01\\stu01\\1.doc')
# print os.path.split('D:\\test\\class01\\stu01\\1.doc')
#
# os.chdir('D:\\')
# print os.listdir('.')
# print os.path.abspath('.')


# def new_report(report_path):
#     lists = os.listdir(report_path)
#     report_list = []
#     for file in lists:
#         file_path = os.path.join(report_path, file)
#         if os.path.isfile(file_path):
#             report_list.append(file)
#     report_list.sort(reverse=True)
#     return os.path.join(report_path, report_list[0])
#
# def new_file(report_path):
#     lists = os.listdir(report_path)
#     report_list = []
#     for file in lists:
#         file_path = os.path.join(report_path, file)
#         if os.path.isfile(file_path):
#             report_list.append(file)
#     report_list.sort(key=lambda fn:os.path.getmtime(report_path+'\\'+fn))
#     return os.path.join(report_path, lists[-1])
#
# print new_report('D:\\report')
# print new_file('D:\\report')

# import shutil
# shutil.copyfile('D:\\report\\20171009235827.html', 'D:\\1.html')
# shutil.copy('D:\\report\\20171009235827.html', 'D:\\1.html')

# shutil.copytree('D:\\report', 'D:\\report_temp')
# shutil.copytree('D:\\report', 'D:\\report_temp', ignore=shutil.ignore_patterns('*.html'))
# shutil.rmtree('D:\\report_temp')

import os



# # writeline(sequence)写入一个包含字符串的序列类型

# file_test = open('D:\\test\\test.txt', 'w')

#

# # 向文件中写入内容

# file_test.writelines(['hello python \n','huicewang.com'])

#

# file_test.close()

#

# # 以读的方式打开一个不存在的文件会报错

# # file_test = open('D:\\test\\new.txt')

#

# # 以写的方式打开一个不存在的文件会？？？

# file_new = open('D:\\test\\new.txt', 'w')

# file_new.write('Hello python')

# file_new.close()

#

# # 以写的方式打开文件，文件会被清空

# file_new = open('D:\\test\\new.txt', 'w')

# file_new.close()

#

#

# # 那如何在打开文件的时候不清空内容，往文件中追加内容呢

# file_test = open('d:\\test\\test.txt','a')

#

# # a：以追加只写的方式打开，不清空文件，在文件末尾加入内容

# file_test.write('我是追加的内容，追加a代表append')

#

# file_test.close()







# 1 文件备份

# source = open('test.png', 'rb')

# context = source.read()

# target = open('test_bak.png', 'wb')

# target.write(context)

# target.flush()

# source.close()

# target.close()





# #2 实现目录递归遍历，查找以.py结尾的文件，并将文件绝对路径存入log.txt文件。

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



file_log = open('D:\\test\\log.txt', 'w+')

for i in res:

    file_log.write(i+'\n')

file_log.close()