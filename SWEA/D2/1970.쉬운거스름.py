testcase=int(input())
coin=[50000,10000,5000,1000,500,100,50,10]

for i in range(testcase):

  coinNum=[0 for i in range(8)]
  N=int(input())

  
  for j in range(8):
    
    if (N/coin[j])>=1:
      coinNum[j]=N//coin[j]
      N=N%coin[j]

  
  print("#",end="")
  print(i+1)
  print( ' '.join(map(str,coinNum)))
