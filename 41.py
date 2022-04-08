T=int(input("搭了幾次電梯："))
list41=[1,]
money=0

for i in range(T):
        s=int(input("樓層："))
        list41.append(s)
for j in range(len(list41)-1):
    if (T>=1 and T<=10) and (list41[j]!=list41[j+1]):
        if list41[j]>list41[j+1]:
            a=list41[j]-list41[j+1]
            money=a*(10)+money
        elif list41[j]<list41[j+1]:
            b=list41[j+1]-list41[j]
            money=b*(20)+money
    else:
        print("輸入錯誤")
        break
money=(list41[0]-1)*20+money
print(money,"元")

