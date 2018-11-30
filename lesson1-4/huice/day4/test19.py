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