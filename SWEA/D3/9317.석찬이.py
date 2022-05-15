testcase=int(input())
for i in range(testcase):
  strLen=int(input())

  correctStr=input()
  copyStr=input()

  cnt=0
  for j in range(strLen):
    if correctStr[j]==copyStr[j]:
      cnt+=1
  
  print("#{} {}".format(i+1,cnt))