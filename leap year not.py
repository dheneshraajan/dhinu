kdr=int(input())
if(kdr%4==0 and kdr%100!=0 or kdr%400==0):
    print("yes")
else:
    print("no")
