
testcase=int(input())


for i in range(testcase):

  result=0
  testCase=list(map(int,input().split()))
  testCase.remove(max(testCase))
  testCase.remove(min(testCase))
  result=round(sum(testCase)/len(testCase))

  print("#",end="")
  print(i+1, result)