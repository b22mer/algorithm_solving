
testcase=int(input())
result=[]
for i in range(testcase):
  sentence=input()
  cnt=0
  check=0  
  while (len(sentence)-1-cnt)-cnt>2:
    # 4인거
    # 3 - 0 = 3
    # 2 1
    
    if sentence[cnt]!=sentence[len(sentence)-1-cnt]:
      check=False
    cnt+=1

  if check==False:
    result.append(0)
  else:
    result.append(1)

print(result)

