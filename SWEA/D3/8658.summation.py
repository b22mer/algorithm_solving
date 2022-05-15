testcase=int(input())
for i in range(testcase):
  testList=input().split()
  testMaxOrMin=[]
  for j in range(10):
    numSource=0
    for k in range(len(testList[j])):
      numSource+=int(testList[j][k])
    testMaxOrMin.append(numSource)

  print("#{} {} {}".format(i+1,max(testMaxOrMin),min(testMaxOrMin)))