from cgitb import reset
from unittest import result


N = int(input())
num = []
for i in range(N):
  num.append(int(input()))

cnt = 0

result=[]

for i in range(N):


  a = 0
  b = 0
  c = 0
  d = 0
  e = 0

  while num[i] != 1:
    if (num[i] % 11 == 0):
      num[i] = num[i]//11
      e += 1
    if (num[i] % 7 == 0):
      num[i] = num[i]//7
      d += 1
    if (num[i] % 5 == 0):
      num[i] = num[i]//5
      c += 1
    if (num[i] % 3 == 0):
      num[i] = num[i]//3
      b += 1
    if (num[i] % 2 == 0):
      num[i] = num[i]//2
      a += 1
    
  result.append([a,b,c,d,e])

for i in range(N):
  print("#",end="")
  print(i+1, ' '.join(map(str, result[i])))