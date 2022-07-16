a = [1, 2, 3, 4, 5]

for i in range(0, len(a)):
    print(a[i])
exit()
# ch7_19.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
    print()         # 換行輸出
    
