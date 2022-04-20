# way1
N = int(input())

coin_3=0
coin_5=0

while N%5!=0 and N>=0:
  N=N-3
  coin_3+=1

if (N<0):
  print(-1)
else:
  coin_5=N/5
  print(int(coin_3+coin_5))

