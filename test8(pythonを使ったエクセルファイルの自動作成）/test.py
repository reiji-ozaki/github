# %%
import openpyxl
import pandas as pd
import glob

import_file_path = 'C:\\プログラミング\\VS code\\test8\\sample.xlsx'
excel_sheet_name = '発注管理表'
export_file_path = 'C:\\プログラミング\\VS code\\test8\\output'
'VS code\\test8\\sample.xlsx'
df_order = pd.read_excel(import_file_path,sheet_name =excel_sheet_name )
df_order

# %%
company_name = df_order['会社名'].unique()
company_name
# %%
type(company_name)
# %%
type(df_order)
# %%
df_order['会社名'] == '株式会社A'
# %%
df_order[df_order['会社名'] == '株式会社A']
# %%
for i in company_name:
  print(i)
# %%
for i in company_name:
    df_order_company = df_order[df_order['会社名'] == i]
    print(df_order_company)

# %%
for i in company_name:
    df_order_company = df_order[df_order['会社名'] == i]
    df_order_company.to_excel(export_file_path+'/'+i+'.xlsx')

