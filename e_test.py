import pandas as pd

data = pd.DataFrame({'fruit': ['apple', 'orange', 'mango', 'melon']})

data_to_excel = pd.ExcelWriter('./~$Book1.xlsx', engine='xlsxwriter')

data.to_excel(data_to_excel, sheet_name='Sheet1')

data_to_excel.save()
