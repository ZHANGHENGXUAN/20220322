#7
import math
tel=input("輸入月租費形式及通話時間為：")
list21=tel.split(",")
list22=list(map(int,list21))

if list22[0]==186:
    if list22[1]*0.09<186:
        print(round(list22[1]*0.09*0.9))
    elif list22[1]*0.09>186:
        print(round(list22[1]*0.09*0.8))
elif list22[0]==386:
    if list22[1]*0.08<386:
        print(round(list22[1]*0.08*0.8))
    elif list22[1]*0.08>386:
        print(round(list22[1]*0.08*0.7))
elif list22[0]==586:
    if list22[1]*0.07<586:
        print(round(list22[1]*0.07*0.7))
    elif list22[1]*0.07>586:
        print(round(list22[1]*0.07*0.6))
elif list22[0]==986:
    if list22[1]*0.06<986:
        print(round(list22[1]*0.06*0.6))
    elif list22[1]*0.06>986:
        print(round(list22[1]*0.06*0.5))
