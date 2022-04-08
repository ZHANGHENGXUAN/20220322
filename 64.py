a=int(input("請輸入第一個要判斷的數字："))
b=int(input("請輸入第二個要判斷的數字："))
count=0
count1=0
if a+2==b:
    for i in range(1,a):
        if a%i==0:
            count+=1
    for j in range(1,b):
        if b%j==0:
            count1+=1

if count!=1 or count1!=1:
    print("N")
elif count==1 or count1==1:
    print("Y")
