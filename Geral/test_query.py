import openpyxl as op

XLSX_PATH = "C:\\ProgramData\\TARGITCloudClient\\TARGITCloudClient.xlsx"

wb_obj = op.load_workbook(XLSX_PATH)
sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(row=1, column=1).value

t = sheet_obj

print(t)
