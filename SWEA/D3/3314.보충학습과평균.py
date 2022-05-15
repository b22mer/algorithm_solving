from doctest import testsource


testcase=int(input())
for i in range(testcase):
  testScore=list(map(int,input().split()))
  
  for j in range(len(testScore)):
    if testScore[j]<40:
      testScore[j]=40
  totalAvg=sum(testScore)//5

  print("#{} {}".format(i+1,totalAvg))