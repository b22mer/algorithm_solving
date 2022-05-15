T=int(input())
for i in range(T):
  N, M= map(int, input().split())
  MaxOrMin=[]
  for j in range(N):
    answerList=input().split()
    MaxOrMin.append(answerList.count("1"))
  firstPersonNum=MaxOrMin.count(max(MaxOrMin))
  
  print("#{} {} {}".format(i+1,firstPersonNum, max(MaxOrMin)))
