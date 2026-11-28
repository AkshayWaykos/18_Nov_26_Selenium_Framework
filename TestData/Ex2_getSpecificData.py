import openpyxl

print("======Approach 1========")

workbook=openpyxl.load_workbook("C:\\Users\\Admin\\PycharmProjects\\PythonProject\\18_Nov_26_Selenium_Framework\\TestData\\DemoTestData.xlsx")
sheet=workbook["Sheet1"]

print(sheet["A1"].value)
print(sheet["A2"].value)
print(sheet["F1"].value)   # for wrong index returns none

print("======Approach 2========")
# Row & col index start with 1

cellValue=sheet.cell(1,2,).value
print(cellValue)

cellValue=sheet.cell(3,4).value
print(cellValue)


