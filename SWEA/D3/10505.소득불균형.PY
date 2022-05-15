
testcase=int(input())

for i in range(testcase):
    N=int(input())
    
    avgList=list(map(int,input().split()))
    totalAvg=sum(avgList)/N
    cnt=0
    for j in range(N):
        if avgList[j]<=totalAvg:
            cnt+=1
    
    print("#{} {}".format(i+1, cnt))
        
        
        
    