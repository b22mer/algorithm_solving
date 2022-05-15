testcase=int(input())
for i in range(testcase):
  testNum=input()
  testList=[]
  for j in range(0,10):
    if (str(j) in testNum) and (str(j) not in testList):
      testList.append(str(j))
  testLen=len(testList)
  print("#{} {}".format(i+1, testLen))