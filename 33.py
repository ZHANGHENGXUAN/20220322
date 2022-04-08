ch=input("國文：")
en=input("英文：")
ma=input("微積分：")
phy=input("體育：")
s=input("程式設計：")
list33=[]
list33.append(ch)
list33.append(en)
list33.append(ma)
list33.append(phy)
list33.append(s)
list3301=list(map(int,list33))
avg=(list3301[0]+list3301[1]+list3301[2]+list3301[3]+list3301[4])/5
#list3302=list3301.sort(reverse=True) list3301內部排序會被改變and不能另外儲存到其他變數 會顯示none
list3302=sorted(list3301,reverse=True)#list3301內部排序不會被改變 可以另外儲存到其他變數
list3303=sorted(list3301,reverse=False)
print("平均分數：",'%.2f' % avg)
print("最高分科目：",list3302[0],"分")
print("最低分科目：",list3303[0],"分")