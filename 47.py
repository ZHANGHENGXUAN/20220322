n=int(input("輸入比數n："))
b=[]
for i in range(n):
    if n<=4:
        metal=input("請輸入：")
        a=metal.split(" ")
        b.append(a)
for j in range(len(b)):
    print("{0}牌得到{1}面".format(b[j][0],b[j][1]))