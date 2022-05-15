T=int(input())
for i in range(T):
    totalStu,submitStu=map(int, input().split())
    chkStu=list(map(int,input().split()))
    notStu=[]
    for j in range(1,totalStu+1):
        if j not in chkStu:
            notStu.append(j)
    
    notStu=list(map(str,notStu))
    print ("#{} {}".format(i+1," ".join(notStu)))
    
    