kdr=int(input())
if(kdr>1):
    for i in range(2,kdr//2):
        if(kdr%i==0):
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
