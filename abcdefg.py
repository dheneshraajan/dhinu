def bubblesort(kdr):
    n=len(kdr)
    for i in range(n):
        for j in range(0,n-1):
            if(kdr[j]>kdr[j+1]):
                kdr[j],kdr[j+1]=kdr[j+1],kdr[j]

kd=int(input())
kdr=list(map(int,input().split()))
bubblesort(kdr)
kdr=kdr[::-1]
kl=""
for i in range(len(kdr)):
    kl=kl+str(kdr[i])
print(int(kl))


