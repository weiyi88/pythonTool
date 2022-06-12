import xlrd
wb = xlrd.open_workbook("./test.xlsx")
sheet_num = wb.nsheets  #获取sheet数量
sheet_name = wb.sheet_names()   #获取所有sheet名称列表
sheet = wb.sheet_by_index(0)    #通过索引获取第一个sheet
# sheet = wb.sheet_by_name('name')  通过名称获取sheet

rows = sheet.nrows  #获取sheet页的行数
cols = sheet.ncols  #获取sheet页的列数

#获取第一行
row_data = sheet.row_values(0)
#获取第一列数据
col_data = sheet.col_values(0)

#或如单元格的数据
one_data = sheet.cell(0,0)      # 第0行第0列数据

# 单元格的值
cell_value = one_data.value

# 单元格的类型
# 0  --  空（empty）
# 1  --  字符串（string）
# 2  --  数字（number）
# 3  --  date（日期）
# 4  --  boolean（布尔值）
# 5  --  error（错误）
cell_type = one_data.ctype


# deep = rows if rows>cols else cols #三元运算符
def printAllData(rows,cols):
    # result = [rows][cols] 坑比python创建二维数组
    result = [[0 for i in range(rows)]for j in range(cols)] #二维数组列表生成式
    for r in range(0,rows-1):
        for c in range(0,cols-1):
            result[r][c]= sheet.cell(r,c).value
    return result

result = printAllData(rows,cols)


