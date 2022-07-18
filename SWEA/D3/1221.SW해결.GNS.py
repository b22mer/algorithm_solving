testcase=int(input())

for i in range(testcase):
    numDic={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    numDicReverse={0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    testNum, testLen=input().split()
    testList=list(input().split())
    resultList=[]

    for j in range(int(testLen)):
        resultList.append(numDic[testList[j]])

    resultList=sorted(resultList)

    for k in  range(int(testLen)):
        resultList[k]=numDicReverse[resultList[k]]

    print(testNum)
    print(" ".join(resultList))
