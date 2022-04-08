a=int(input("請輸入a："))
b=int(input("請輸入b："))
c=int(input("請輸入c："))

x1=((-b)+((b**2-4*a*c)**0.5))/(2*a)
x2=((-b)-((b**2-4*a*c)**0.5))/(2*a)
if ((b**2)-(4*a*c))>0:
    print('%d'%x1,'%d'%x2)
elif ((b**2)-(4*a*c))<0:
    print("0")
elif ((b**2)-(4*a*c))==0:
    print('%d' %x1)