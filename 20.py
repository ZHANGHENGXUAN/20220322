#20
group=input("組數為：")
list20=[]
list20.split(" ")
for i in range(group):
    tickets=input("張數：")
    list20.append(int(tickets))
    list20[0]*250
    list20[1]*175
    print("第",i,"組應收費用：",list20[0]*250+list20[1]*175)