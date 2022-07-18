t=int(input())
for i in range(t):
  testCase=list(input())
  H=int(input())
  testLocation= list(map(int,input().split()))
  resultList=[]
  for j in range(H):
    resultList

    testCase.insert(testLocation[j],"-")
  
  print("#{} {}".format(i+1, "".join(testCase)))

#   w o - - w  


# testList=[0, 0, 0, 0]
# testList.insert(5,"=")
# print(testList)