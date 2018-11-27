import xlrd
data = xlrd.open_workbook('test.xls')
print(type(data))

print(type(data.sheets()))
for sheet in data.sheets():
    print(type(sheet))

sheet = data.sheet_by_index(0)
print(sheet.row_values(0))
print(sheet.col_values(0))

sheet = data.sheet_by_name('Case01')
print(type(sheet.cell(0,0)))
print(type(sheet.cell(0,0).value))
print(sheet.nrows)
print(sheet.ncols)

