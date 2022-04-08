n=int(input("輸入n值："))
dic={}
for i in range(n):
    name=input("請輸入姓名：")
    Email=input("請輸入電子郵件：")
    dic[name]=Email #dic[key]=value
look=input("請輸入要查詢電子郵件的姓名：")
print(look,"電子郵件帳號為",dic.get(look)) #get取值 ==> dic.get(key)