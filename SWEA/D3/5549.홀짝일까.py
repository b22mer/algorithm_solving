
testcase=int(input())
for i in range(testcase):
  testCase=int(input())

  if (testCase%2!=0):
    result="Odd"
  else:
    result="Even"
  print("#{} {}".format(i+1, result))