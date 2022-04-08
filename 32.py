M=input("小明身上有幾元：")
N=int(input("販賣機有幾種飲料："))
count=0
for i in range(N):
    P=input("價錢：")
    if M>=P:
        count+=1
    else:
        count+=0
print(count)