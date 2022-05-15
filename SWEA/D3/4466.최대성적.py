T = int(input())
for i in range(T):
    stuNum, choiceNum=map(int,input().split())
    scoreList=list(map(int,input().split()))
    resultList=list(sorted(scoreList,reverse=True))
    result=0
    for j in range(choiceNum):
        result+=resultList[j]
    print("#{} {}".format(i+1, result))