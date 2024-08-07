import os
import openpyxl

# Function to append data to Excel
def append_to_excel(data, filename="output.xlsx"):
    if not os.path.exists(filename):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        headers = [
            "Name", "Location", "Joined Date", "Invested States", "Days of Livehood",
            "Lives Impacted", "Credit Histories", "Top Investment State 1", "Top Investment State 2",
            "Top Investment State 3", "Top Investment Sector 1", "Top Investment Sector 2",
            "Top Investment Sector 3", "Amplified Impact Allieds", "Amplified Lives Impacted",
            "Amplified Livelihood", "Profile URL"
        ]
        sheet.append(headers)
    else:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active

    for data_dict in data:
        row = [
            data_dict.get("Name", ""),
            data_dict.get("Location", ""),
            data_dict.get("Joined Date", ""),
            data_dict.get("Invested States", ""),
            data_dict.get("Days of Livehood", ""),
            data_dict.get("Lives Impacted", ""),
            data_dict.get("Credit Histories", ""),
            data_dict.get("Top Investment State 1", ""),
            data_dict.get("Top Investment State 2", ""),
            data_dict.get("Top Investment State 3", ""),
            data_dict.get("Top Investment Sector 1", ""),
            data_dict.get("Top Investment Sector 2", ""),
            data_dict.get("Top Investment Sector 3", ""),
            data_dict.get("Amplified Impact Allieds", ""),
            data_dict.get("Amplified Lives Impacted", ""),
            data_dict.get("Amplified Livelihood", ""),
            data_dict.get("Profile URL", "")
        ]
        sheet.append(row)
    
    workbook.save(filename)