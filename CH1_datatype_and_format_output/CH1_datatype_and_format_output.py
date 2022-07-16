import logging
from sys import getsizeof
import pandas as pd
a = pd.DataFrame({"A":[],"學生":[]})

if a.empty:
    print("沒有資料")
else:
    print("資料處理")
"""
基礎型態
"""
##########################
# 整數 int
x = 10
print("整數 int, x={}, tpye is:{}, size is :{}\n{}".format(x, type(x), getsizeof(x), "="*10))
##########################
# 浮點數 float
x = x + 5.5
print("浮點數 float, x={}, tpye is:{}, size is :{}\n{}".format(x, type(x), getsizeof(x), "="*10))
##########################
# 布林 bool(注意，在條件控制後續使用上，True、False = 1、0)
x = True
print("布林 bool, x={}, tpye is:{}, size is :{}\n{}".format(x,type(x), getsizeof(x), "="*10))
##########################
# 字串 str
x = "hello"
print("字串 str, x={}, tpye is:{}, size is :{}\n{}".format(x, type(x), getsizeof(x), "="*10))

##########################
# 補充-格式化輸出 (常用)
print("補充-格式化輸出 (常用)\n{}".format("="*10))
print("Hello, my name is sean, I'm %s years old." %('twenty-eight'))  # %d 格式化輸出字串
print("Hello, my name is sean, I'm %d years old." %(28))  # %d 格式化輸出整數
print("Hello, my name is sean, I'm %f years old." %(28.6))  # %f 格式化輸出浮點數
print("Hello, my name is sean, I'm %10d years old." %(28))  # %f 格式化控制整數位置
print("Hello, my name is sean, I'm %-10d years old." %(28))  # %f 格式化控制整數位置
print("Hello, my name is sean, I'm %-10d years old." %(28.6))  # %f 格式化控制整數位置
print("Hello, my name is sean, I'm %3.4f years old." %(28.699999999999999999999))  # %f 格式化輸出浮點數!!!!!!!!!!!!!!!!!!!!!!!!!!!
print("Hello, my name is sean, I'm %-10.10f years old." %(28.6))  # %f 格式化輸出浮點數
print("Hello, my name is sean, I'm {} years old.".format(28))  # format 函數!!!!!!!!!!!!!!!!!!!!!!!!!
my_age = 28
my_mom_age = 50
print("Hello, my name is sean, I'm {} years old.".format(my_age))  # format 函數
print("Hello, my name is sean, I'm {} years old, and My mom is {} years old".format(my_age, my_mom_age))  # format 函數
##########################
# 補充-溢出字元 (特殊符號，ex, 空白、...)
print("補充-溢出字元 (特殊符號，ex, 空白、...)\n{}".format("="*10))
print("Hello, my name is \nsean")  # 換行
print("Hello, my name is \\sean")  # 右斜線
print("Hello, my name is sean\a")  # B一聲
print("Hello, my name\b is sean")  # backspace
print(r"Hello, my name is \nsean") # 字串前面加r，使溢出字元無效
##########################
# 補充-字串操作
print("補充-字串操作")
print("你好"*3)  # 字串複製
print("你好"+"我是羅智翔"+"."*3+"其實我是時間管理大師")  # 字串複製
print("\n{}".format("="*10))
##########################
print("補充-基礎物件")
descript = """python中的基礎物件有， \n(1) 列表 list: 有序、可變容器，常用\n(2) 字典 dict: 可透過KEY值提取數值的、可變容器，常用\n(3) 集合Set:無序且元素是唯一值、且不可變\n(4) 元組 Tuple: 不可動容器，很少使用"""
print("{}\n{}".format(descript,"="*10))
##########################
print("補充-資料輸入")
a = input("請輸入年齡:")
print("我今年{}歲".format(a))
print("\n{}".format("="*10))
##########################
