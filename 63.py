n=int(input("請輸入正整數n："))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect")
elif sum>n:
    print("abundant")
elif sum<n:
    print("deficient")