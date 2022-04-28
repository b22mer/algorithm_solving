
N= int(input())
resultData=[]
for i in range(N):

  numLen=int(input())
  numList=list(map(int, input().split()))
  numList.sort()
  resultData.append(numList)

for j in range(N):
  print("#",end="")
  print(j+1, ' '.join(map(str, resultData[j])))




  