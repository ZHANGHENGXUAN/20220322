n=int(input("小狗可能跑到幾個地方："))
count=0
for i in range(n):
    k=int(input("與家裡的距離："))
    if n>=2 and n<=10:
        if k%9==0 or k%11==0:
            count+=1
            print("第",count,"個點",k)
        else:
            count+=1
    print()