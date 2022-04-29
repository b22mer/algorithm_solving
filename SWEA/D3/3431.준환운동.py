

testcase=int(input())

for i in range(testcase):

  L,U,X=map(int, input().split())
  result=0

  if L<=X and X<=U:
    result=0
  elif L>X:
    result=L-X
  elif X>U:
    result=-1
  
  print("#",end="")
  print(i+1, result)