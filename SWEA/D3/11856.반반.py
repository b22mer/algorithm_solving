from unittest import result


TC=int(input())
for i in range(TC):
  testString=list(input())
  result="Yes"
  if testString.count(testString[0]) >2 or testString.count(testString[0]) <2:
    result="No"
  elif len(set(testString))!=2:
    result="No"
  
  print("#{} {}".format(i+1,result))
  

