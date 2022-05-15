from imghdr import tests


testcase=int(input())
for i in range(testcase):
    N,M = map(int, input().split())
    testList=[]
    for j in range(1,N+1):
        for k in range(1,M+1):
            testList.append(j+k)
    testList=list(set(testList))
    print(testList)
    resultList=[0 for i in range(len(testList))]
    for j in range(1,N+1):
        for k in range(1,M+1):
            resultList[testList.index(j+k)]+=1
    print(resultList)
  
                    
    # testList=list(set(testList))
    
    # print(testList)
    