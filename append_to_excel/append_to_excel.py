import os
import openpyxl

# Function to append data to Excel
def append_to_excel(data, filename="output.xlsx"):
    if not data:
        return  # Если данных нет, ничего не делаем

    if not os.path.exists(filename):
        workbook = openpyxl.Workbook()  
        sheet = workbook.active
        headers = list(data[0].keys())  # Берем заголовки из первого словаря
        sheet.append(headers)
    else:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]  # Получаем заголовки из первой строки

    for data_dict in data:
        row = [data_dict.get(col, "") for col in headers]  # Заполняем строки значениями
        sheet.append(row)
    
    workbook.save(filename)
