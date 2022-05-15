for i in range(10):
    dumpNum=int(input())
    testList=list(map(int,input().split()))
    result=0
    for j in range(dumpNum):
        testList[testList.index(max(testList))]-=1
        testList[testList.index(min(testList))]+=1
    maxNum=max(testList)
    minNum=min(testList)
    result=maxNum-minNum
    print("#{} {}".format(i+1, result))