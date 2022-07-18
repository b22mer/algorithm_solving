T= int(input())
for i in range(T):
  testString=input()
  stringLen=len(testString)
  resultList=[]

  for j in range(stringLen):
    if testString.count(testString[j]) %2!=0:
      resultList.append(testString[j])
  resultList=list(sorted(resultList))
  if (len(resultList) ==0):
    resultList.append("Good")
  
  print("#{} {}".format(i+1,"".join(resultList)))
