import openpyxl

wordbook=openpyxl.load_workbook("C:\\Users\\Admin\\PycharmProjects\\PythonProject\\18_Nov_26_Selenium_Framework\\TestData\\DemoTestData.xlsx")
sh=wordbook["Sheet1"]

rowSize=sh.max_row
print(rowSize)

colSize=sh.max_column
print(colSize)

