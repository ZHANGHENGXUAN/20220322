num=int(input("輸入查詢組數："))
for i in range(num):
    group1=input("請輸入帳號：")
    group2=input("請輸入密碼：")
    if group1=="123" and group2=="456":
        print("9000")
    elif group1=="456" and group2=="789":
        print("5000")
    elif group1=="789" and group2=="888":
        print("5000")
    elif group1=="336" and group2=="558":
        print("6000")
    elif group1=="775" and group2=="666":
        print("12000")
    elif group1=="566" and group2=="221":
        print("7000")
    else:
        print("error")
    print()