T=int(input())
for i in range(T):
  takeChar=list(input())
  cnt=0
  testList=list(takeChar)
  for j in takeChar:
    if testList.count(j)%2!=0:
      testList.remove(j)
      cnt+=1
  print("#{} {}".format(i+1, cnt))