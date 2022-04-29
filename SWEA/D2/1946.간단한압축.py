testcase = int(input())

for i in range(testcase):

  N = int(input())
  testString = ""

  for j in range(N):
    testAlpha, testLen = input().split()
    testString += testAlpha*int(testLen)

  resultString = list(testString)
  resultLen = len(resultString)
  print("#", end="")
  print(i+1)

  for x in range(resultLen):


    if(x) % 10 == 0 and x!=0:
      print("")
    print(resultString[x],end="")
  print("")
