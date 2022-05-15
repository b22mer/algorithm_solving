T= int(input())
for i in range(T):
    K=int(input())
    testList=[]
    for j in range(K):
        writeNum=int(input())
        if writeNum==0:
            testList.pop()
        else:
            testList.append(writeNum)
    result=sum(testList)
    print("#{} {}".format(i+1,result))