

testcase=int(input())

sdocu=[0 for i in range(9)]
result=[]
for i in range(testcase):
  chk=0
  for j in range(9):
    sdocu[j]=list(map(int,input().split()))
   
  #큰 가로줄 체크
    if sorted(sdocu[j])!=[1,2,3,4,5,6,7,8,9]:
      chk+=1
  
  #큰 세로줄 체크
  for x in range(9):
    testSero=[]
    for y in range(9):
      testSero.append(sdocu[y][x])
    if sorted(testSero)!=[1,2,3,4,5,6,7,8,9]:
      chk+=1
  
  #첫번째 세뭉탱이
  
  for z in range(3):
    testSquare=[]
    for x in range(3):
      for y in range(3):
        testSquare.append(sdocu[x+3*z][y])
      # print("첫번째 세뭉:", testSquare)
    if sorted(testSquare)!=[1,2,3,4,5,6,7,8,9]:
      chk+=1

  #두 번째 세뭉탱이
  for z in range(3):
    testSquare=[]
    for x in range(3):
      for y in range(3):
        testSquare.append(sdocu[x+3*z][y+3])
      # print("두번째 세뭉:", testSquare)
    if sorted(testSquare)!=[1,2,3,4,5,6,7,8,9]:
      chk+=1

  #세 번째 세뭉탱이
  for z in range(3):
    testSquare=[]
    for x in range(3):
      for y in range(3):
        testSquare.append(sdocu[x+3*z][y+6])
      # print("세번째 세뭉:", testSquare)
    if sorted(testSquare)!=[1,2,3,4,5,6,7,8,9]:
      chk+=1



  if chk==0:
    result.append(1)
  else:
    result.append(0)



for i in range(testcase):
    print("#", end="")
    print(i+1, result[i])

