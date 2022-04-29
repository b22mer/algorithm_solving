testcase=int(input())

for i in range(testcase):
  caseNum=int(input())
  scoreList=list(map(int, input().split()))
  max=0
  chk=0
  for k in range(101):
    if (max<=scoreList.count(k)):
      max=scoreList.count(k)
      chk=k
  
  print("#",end="")
  print(caseNum, chk)
  
  

