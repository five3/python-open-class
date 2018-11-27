import xlrd
import json

book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_name('Bugs')

# 先取出项目名
# 遍历首行，找到内容为 项目名 的列数，将该列值取出放入list
r_name = sheet.row_values(0)
number_index = r_name.index('数量')
pro_index = r_name.index('项目名')

project_name = sheet.col_values(pro_index)
project_name.pop(0)

# 项目名去重
project_name = sorted(list(set(project_name)), key = project_name.index)
print(project_name)

data = {}
r_name = sheet.col_values(0)
for p_name in project_name:
    number = 0
    for n in range(1, len(r_name)):
        if r_name[n] == p_name:
            number += int(sheet.cell(n, number_index).value)
    data[p_name] = number

print(data)
print(json.dumps(data, indent=4))
