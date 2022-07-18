T=int(input())
for i in range(T):
  testList=[]
  max=0
  for j in range(5):
    testList.append(list(input()))
    if max<len(testList[j]):
      max=len(testList[j])

  for x in range(5):
    for y in range(max-len(testList[x])):
      testList[x].append("*")

  resultList=[]

  for j in range(max):
    for k in range(5):
      resultList.append(testList[k][j])

  resultList=[i for i in resultList if i not in "*"]
  print("#{} {}".format(i+1,"".join(resultList)))

