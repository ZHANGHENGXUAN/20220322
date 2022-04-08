ID=input("請輸入A的好友：").split(" ")
ID2=input("請輸入B的好友：").split(" ")
s1=set(ID)
s2=set(ID2)
s3=s1&s2
s4=len(s3)
print(s4)

