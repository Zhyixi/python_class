"""1. 請設計一個程式，如果輸入是負值，則將它改為正值輸出，如果輸出是正值則改為負值輸出，若輸入為非數字，則輸出錯誤警告"""

while True:
    a = input("plz enter a num")
    try:
        a = int(a)
        if a < 0:
            print(abs(a))
        elif a >= 0:
            print(a * (-1))
    except:
        if a == 'q':
            break
        else:
            print("輸入錯誤，請輸入數字")
    finally:
        print("結束")
