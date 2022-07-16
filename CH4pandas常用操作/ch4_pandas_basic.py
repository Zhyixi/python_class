
import pandas as pd  # 導入模組並給予別名 
import numpy as np
# example1: 檢查版本
print("pandas 當前版本:{}".format(pd.__version__))

# example2: 建立Series物件與提取數值
series_obj = pd.Series(data=[1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])
print("位置索引:\n{}".format(series_obj.index))
print("數值array:\n{}".format(series_obj.values))
print("使用數字位置提取，series_obj[2]:\n{}".format(series_obj[2]))
print("使用數字位置切片，注意包含起始位置不含結束，series_obj[1:3]:\n{}".format(series_obj[1:3]))
print("使用文字位置提取，series_obj['d']:\n{}".format(series_obj['d']))
print("使用文字位置切片，注意包含起始與結束位置，series_obj['a':'b']:\n{}".format(series_obj['a':'b']))

# example3: Series物件的字典方法
print("將可迭代物件強制轉為陣列list，list(series_obj.iteritems()):\n{}".format(list(series_obj.iteritems())))
# 可透過迴圈取出對應數值
for idx, value in series_obj.iteritems():
    print(f"index:{idx}, values:{value}")

# example4: Series進行運算
series_obj2 = pd.Series(data=[20,30,40,50,60], index=['b', 'c', 'd', 'e', 'f'])
series_obj_res = series_obj + series_obj2
print("兩個series相加:\n{}".format(series_obj_res))


# example5: 建立DataFrame的各種方法
df1 = pd.DataFrame() # 空的表格
df2 = pd.DataFrame(columns=["姓名", "地址"]) # 空的，但是有columns name
df3 = pd.DataFrame(data=[[1,2],['a','b']])  # 有數值，但沒有columns name
df4 = pd.DataFrame(data=[['吳寶春',"台北市"],["馬英九","台中市"]], columns=["姓名", "地址"])  # 有數值，也有columns name
df5 = pd.DataFrame(data={"姓名":['吳寶春', "馬英九", "陳水扁"], "得票率":[0,100,200]})  # 以dict建立
df6 = pd.read_excel('file/test_file.xlsx')  # 讀取excel
df7 = pd.read_csv('file/test_file.csv')  # 讀取csv
df8 = pd.read_csv('file/test_file.txt', sep='\t', lineterminator='\n',encoding='utf-16')  # 讀取txt
df8.set_index("日期", inplace=True)

print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print(df7)
print(df8)





