T=int(input("請輸入有幾筆測試資料："))
for i in range(T):
    m1=int(input("第一個："))
    m2=int(input("第二個："))
    m3=int(input("第三個："))
    m4=int(input("第四個："))
    if ((m4-m3)==(m3-m2)) and ((m3-m2)==(m2-m1)):
        print("第五個：",m4+(m4-m3))
        print("此為等差數列")
    elif ((m4/m3)==(m3/m2)) and ((m3/m2)==(m2/m1)):
        print("第五個：",'%d' % (m4*(m4/m3)))
        print("此為等比數列")
    print()