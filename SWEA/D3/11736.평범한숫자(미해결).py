
TC=int(input())
for i in range(TC):
  N=int(input())
  testList=list(map(int, input().split()))
  maxNum=max(testList)
  minNum=min(testList)
  chk=0 
  for j in range(2, N-1):
    if testList[j-1]!=maxNum or testList[j-1]!=minNum :
      chk+=1
  
  print("#{} {}".format(i+1, chk))