for i in range(10):
    pwNum= int(input())

    pwList=list(map(int, input().split()))


    while pwList.find(0)==-1:
        
        for j in range(8):
            pwList[j]=pwList[j]
            
    # while pwList[0]!=0:
    #     cnt=0
    #     for j in range(5):
    #         cnt=cnt%5+1
    #         pwList[j]=pwList[j]-cnt
    #         firstNUM=pwList[j]
    #         del(pwList[0])
    #         pwList.append(firstNUM)
    
    # print(pwList)
                
    
    
    1 2 3 4 5 6 7 8
    
    1 2 3 4 5 1 2 3 4 5 
    1 2 3 4 5 1 2 3 4 5 
    1 2 3 4 5 