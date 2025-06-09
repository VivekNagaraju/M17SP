import openpyxl


filepath = "C:\\Users\\admin\\Desktop\\OrangeHRM_Login_DDT.xlsx"
my_workbook = openpyxl.load_workbook(filepath)
# my_active_sheet = my_workbook.active # Get the currently active sheet
my_active_sheet = my_workbook["Sheet1"] # Get the sheet by name
total_rows = my_active_sheet.max_row
print(total_rows)

total_columns = my_active_sheet.max_column
print(total_columns)

for i in range(2, total_rows+1):
    username = my_active_sheet.cell(i, 1).value
    password = my_active_sheet.cell(i, 2).value
    print(username, password)

