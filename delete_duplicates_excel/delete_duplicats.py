import pandas as pd

def remove_duplicate_rows_by_profile_url(input_file, output_file, columns_to_delete, sheet_name='Sheet'):
    # Чтение данных из Excel файла
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    # Удаление дубликатов на основе значения в столбце 'profile_url'
    df_unique = df.drop_duplicates(subset=[columns_to_delete])

    # Запись данных без дубликатов обратно в Excel файл
    df_unique.to_excel(output_file, index=False)

    print(f'Duplicates removed. Clean data saved to {output_file}')

# Пример использования
name_of_xlsx = "output.xlsx"
output_name_of_xlsx = "output_duplicates_deleted.xlsx"
column_to_delete = "Profile URL"
remove_duplicate_rows_by_profile_url(name_of_xlsx, output_name_of_xlsx, column_to_delete)