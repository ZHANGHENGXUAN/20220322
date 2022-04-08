#3
year=int(input("請輸入西元年："))
year1=year-1911
year3=year1%12
if year3==1:
    print("rat")
elif year3==2:
    print("ox")
elif year3==3:
    print("tiger")
elif year3==4:
    print("rabbit")
elif year3==5:
    print("dragon")
elif year3==6:
    print("snake")
elif year3==7:
    print("horse")
elif year3==8:
    print("sheep")
elif year3==9:
    print("monkey")
elif year3==10:
    print("rooster")
elif year3==11:
    print("dog")
elif year3==12 or year==0:
    print("pig")
