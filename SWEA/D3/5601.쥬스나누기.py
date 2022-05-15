testcase=int(input())
for i in range(testcase):
  personNum=int(input())
  print("#{}".format(i+1), end=" ")
  for j in range(personNum):
    print("1","/",str(personNum),sep="", end=" ")
  print()
