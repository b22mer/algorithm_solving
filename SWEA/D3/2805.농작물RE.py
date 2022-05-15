testcase=int(input())
for i in range(testcase):
    repeatNum=int(input())
    testList=[]
    sum=0
    for j in range(repeatNum):
        testList.append(list(input()))
    
    for j in range((repeatNum//2)+1):

        sum+= testList[j][(repeatNum//2)]