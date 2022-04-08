T=int(input("班級數量："))
list44=[]
for i in range(T):
    if T>=1 and T<=10:
        num=int(input("人數："))
        list44.append(num)
    else:
        break
    list44.sort(reverse=True)
print(list44[0])