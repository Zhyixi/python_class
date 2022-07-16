"""python教成第0章第2節: 條件控制"""

age = input("請輸入年齡: ")
if (int(age) < 20):
    print("你年齡太小")
    print("需年滿20歲才可以購買菸酒")
#########################
#
print("輸出絕對值")
num = input("請輸入任意整值: ")
x = int(num)  # 強制型態轉換
if (int(x) < 0):
    x = abs(x)
print("絕對值是 %d" % int(x))

#########################
age = input("請輸入年齡: ")
if (int(age) < 20):
    print("你年齡太小")
    print("需年滿20歲才可以購買菸酒")
else:
    print("歡迎購買菸酒")
#########################
# 奇數偶數判斷
print("奇數偶數判斷")
num = input("請輸入任意整值: ")
rem = int(num) % 2
if (rem == 0):
    print("%d 是偶數" % int(num))
else:
    print("%d 是奇數" % int(num))
#########################
print("計算最終成績")
score = input("請輸入分數: ")
sc = int(score)
if (sc >= 90):
    print(" A")
elif (sc >= 80):
    print(" B")
elif (sc >= 70):
    print(" C")
elif (sc >= 60):
    print(" D")
else:
    print(" F")
#########################
# 計算票價
print("計算票價")
age = input("請輸入年齡: ")
age = int(age)
ticket = 100

if age >= 80 or age <= 6:
    ticket = ticket * 0.2
    print("票價是: %d" % ticket)
elif age >= 60 or age <= 12:
    ticket = ticket * 0.5
    print("票價是: %d" % ticket)
else:
    print("票價是: %d" % ticket)
#########################
# 計算票價程式
print("計算票價")
age = input("請輸入年齡: ")
age = int(age)
ticket = 100
if age >= 80 or age <= 6:
    ticket = ticket * 0.2
    print("票價是: %d" % ticket)
elif age >= 60 or age <= 12:
    ticket = ticket * 0.5
    print("票價是: %d" % ticket)
else:
    print("票價是: %d" % ticket)
