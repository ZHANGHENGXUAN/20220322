a=str(input("請輸入自傳(至少10個字)"))
a1=a.split(" ")
b1=set(a1[0])
b2=set(a1[1])
c=b1&b2
c.remove("，")
c.remove("。")
print(c)
