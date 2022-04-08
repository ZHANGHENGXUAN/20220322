z=0
while z==0:
    a=str(input("檢測的字串(end結束)："))
    a.split(" ")
    if a=="end":
        z+=1
        print("檢測結束")
    else:
        ph=str(input("檢測的單一字元："))
        ph1=a.count(ph)
        print("字元",ph,"出現次數為：",ph1)