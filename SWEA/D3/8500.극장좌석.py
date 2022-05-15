T=int(input())
for i in range(T):
    personNum=int(input())
    seatList=list(map(int,input().split()))
    seatList=sorted(seatList,reverse=True)
    total=0
    for j in range(len(seatList)):
        if j==0:
            total+=seatList[j]*2
        else:
            total+=seatList[j]
    total+=personNum
    
    print("#{} {}".format(i+1,total))    
    


