#2
degree=int(input("請輸入一個度數(正整數)"))
if degree<=120:
    print("summer months:",'%.2f' % (degree*2.10))
    print("Non-summer months:",'%.2f' % (degree*2.10))
elif (degree>=121 and degree<=330):
    print("summer months:",'%.2f' % (degree*3.02))
    print("Non-summer months:",'%.2f' % (degree*2.68))
elif (degree>=331 and degree<=500):
    print("summer months:",'%.2f' % (degree*4.39))
    print("Non-summer months:",'%.2f' % (degree*3.61))
elif (degree>=501 and degree<=700):
    print("summer months:",'%.2f' % (degree*4.97))
    print("Non-summer months:",'%.2f' % (degree*4.01))
elif (degree>=701):
    print("summer months:",'%.2f' % (degree*5.63))
    print("Non-summer months:",'%.2f' % (degree*4.50))