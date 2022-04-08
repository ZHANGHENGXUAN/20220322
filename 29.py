a=input("甲方的數字：")
b=input("乙方的數字：")

for i in range(len(a)):
    if a[i]=="1" and b[i]=="5":
        print("贏",end="")
    elif a[i]<b[i] or (a[i]=="5" and b[i]=="1"):
        print("輸",end="")
    elif a[i]>b[i]:
        print("贏",end="")
    elif a[i]==b[i]:
        print("和",end="")
print()
            
        






