import pandas as pd
import numpy as np
import os
import pathlib
import os
from ToolPackage.DB_Connection import DbConnector
# from "套件" import "模組"
# from "套件.模組" import "Class" or "function"

ys_economic_db = DbConnector(db_type='postgres', database_info='ys_economic', user_info='postgres', password_info='951612',
                 host_info='localhost', port_info='5432')
# 設定顯示選項
pd.set_option("display.max_rows", 1000000)  # 設定可顯示的最大列數
pd.set_option("display.max_columns", 1000000)  # 設定可顯示的最大行數
pd.set_option('display.width', 500000)  # 設定可顯示的最大寬度
# # 讀取文件
# # df = pd.read_excel('{}/file/schedule.xlsx'.format(os.getcwd()))[['ID_NO', "CURRENT_SHOP_CODE", 'WORK_TIME']]
# # ys_economic_db.exe_sql(sql_list=["""create schema analyst;"""])
# # ys_economic_db._close_cursor()
# # ys_economic_db._close_connection()
# # df.to_sql(name="test_table", schema="analyst", index=False, if_exists='append', con=ys_economic_db.engine)
[df] = ys_economic_db.read_from_db(sql_list=["""select * from analyst.test_table;"""])

# 進階:pivot
"""
index: 族群
values: 觀察的值，統計用
columns: 各個族群的分類
"""
# print(df[df["ID_NO"]=="ZB532L05"])

# pvt = df.pivot_table(values='WORK_TIME',
#                      index='ID_NO',
#                      columns='CURRENT_SHOP_CODE', fill_value="NAN")
print("read csv")
df = pd.read_csv('{}/file/Chinese_Income_Statement.csv'.format(os.getcwd())).head(100)
# print(df.head(100))

pvt = df.pivot_table(values=["net profit", "net profit growth"],
                     index='ticker',
                     columns=["Date"], aggfunc=['min', 'max'], fill_value=0)

pvt = df.pivot_table(values=["net profit", "net profit growth"],
                     index='ticker',
                     columns=["Date"], aggfunc={'net profit': np.mean, 'net profit growth': [min, max]}, fill_value=0)
# 進階:agg
# 範例數據
df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])
# 0 = row, 1 = column
print(df.agg(['sum', 'min'], axis=0))
# 進階:aply
print(df.apply(np.sqrt))
# 進階aply:匿名函數
# lambda parameter_list: expression
print(df.apply(lambda x : x**2))

