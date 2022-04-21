
testcase=int(input())
result=[]

for i in range(testcase):
  
  case=int(input())
  check=[]
  cnt=1
  while len(check)<10:

    bikyo=case*cnt
    temp=str(bikyo)
    
    for j in range(len(temp)):
      
      if temp[j] in check:
        continue
      else:
        check.append(temp[j])
        if len(check)==10:
          result.append(bikyo)
          
    
    cnt+=1

for i in range(testcase):
  print("#",end="")
  print(i+1, result[i])