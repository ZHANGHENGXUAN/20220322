km=float(input("請輸入路程公里數(km)："))
if km > 1.5:
    if (km-1.5)<=0.25:
        print("所需車資為：",75+5)
    elif (km-1.5)>0.25:
        if (km-1.5)%0.25!=0:
            pay=(km-1.5)//0.25+1
            print('%d' % (pay*5+75))
        else:
            pay=(km-1.5)//0.25
            print('%d' % (pay*5+75))
else:
    print("所需車資為：",75)