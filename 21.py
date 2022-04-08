#21
list2121=[[123,"Tom","DTGD"],[456,"Cat","CSIE"],[789,"Nana","ASIE"],[321,"Lim","DBA"],[654,"Won","FDD"]]
id21=input("輸入查詢學號為：")
if id21=="123":
    print("學生資料為：",list2121[0][0],list2121[0][1],list2121[0][2])
elif id21=="456":
    print(list2121[1][0],list2121[1][1],list2121[1][2])
elif id21=="789":
    print(list2121[2][0],list2121[2][1],list2121[2][2])
elif id21=="321":
    print(list2121[3][0],list2121[3][1],list2121[3][2])
elif id21=="654":
    print(list2121[4][0],list2121[4][1],list2121[4][2])