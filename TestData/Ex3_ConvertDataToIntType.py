import openpyxl

workbook=openpyxl.load_workbook("C:\\Users\\Admin\\PycharmProjects\\PythonProject\\18_Nov_26_Selenium_Framework\\TestData\\DemoTestData.xlsx")
sheet=workbook.active

# Read value from first cell (A1)
cellValue = sheet.cell(2,3).value

# Convert to integer
int_value = int(cellValue)
print(int_value)

