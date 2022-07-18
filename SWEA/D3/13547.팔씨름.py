T=int(input())
for i in range(T):
  testString=list(input())
  otherLen=15-len(testString)

  if (testString.count("o")+otherLen>=8):
    result="YES"
  else: 
    result="NO"
  
  print("#{} {}".format(i+1,result))
  
  
  


