# def list_chunk(lst, n):
#     return [lst[i:i+n] for i in range(0, len(lst), n)]


for i in range(10):
  proNum=int(input())
  squareX=[]
  for a in range(100):
    squareX.append(list(map(int,input().split())))
  max=0

  # 행체크
  for j in range(100):
    if max<sum(squareX[j]):
      max=sum(squareX[j])
  
  #열체크
  for x in range(100):
    testSum1=0
    for y in range(100):
      testSum1+=squareX[y][x]
    if max<testSum1:
      max=testSum1    
    
  # 오른쪽 대각선체크
  testSum2=0
  for z in range(100):
    testSum2+=squareX[z][z]
  if max<testSum2:
    max=testSum2    
    
  # 왼쪽 대각선 체크
  testSum3=0
  for c in range(100):
    testSum3+=squareX[c][99-c]
  if max<testSum3:
    max=testSum3    

  print("#{} {}".format(proNum,max))  


#   # 0 99
  # 1 98
  # 2 97
  # ...
  # 99 0
