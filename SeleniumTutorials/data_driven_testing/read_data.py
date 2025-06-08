import openpyxl

filepath = "C:\\Users\\admin\\Desktop\\OrangeHRM_Login_DDT.xlsx"
my_workbook = openpyxl.load_workbook(filepath)
my_active_sheet = my_workbook.active
total_rows = my_active_sheet.max_row
print(total_rows)

total_columns = my_active_sheet.max_column
print(total_columns)