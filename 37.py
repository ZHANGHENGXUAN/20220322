n=int(input("變數n:"))
print(n,end=" ")
while n!=1 and n>0 and n<1000000:
    if n%2!=0:
        n=n*3+1
        print('%d' %n,end=" ")
    elif n%2==0:
        n=n/2
        print('%d' %n,end=" ")
print()