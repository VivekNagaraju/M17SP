import openpyxl

filepath = "C:\\Users\\admin\\Desktop\\OrangeHRM_Login_DDT.xlsx"
my_workbook = openpyxl.load_workbook(filepath)
my_active_sheet = my_workbook["Sheet1"]

my_active_sheet.cell(2, 3).value="Pass"

my_workbook.save(filepath)