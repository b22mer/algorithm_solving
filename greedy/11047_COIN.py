
from calendar import c


N, K = input().split()
# 10 4200

i = 0
N = int(N)
K = int(K)

coin = [0 for i in range(N)]
# 동전종류 재료
while i < N:
   element = int(input())
   coin[N-i-1]=element
   i = i+1
# [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

coinFinder = 0
bill=0
# 본 돈이 0이 될때까지 진행
while 0 != K:
  #먼저 큰단위의 동전으로 나눴을때 몫이 1보다 작다면 다음 동전으로 그냥 넘어감
  if (K/coin[coinFinder]<1):
    coinFinder+=1
    continue
  #1보다 크면 거기서 나머지가 없는경우가 존재하는데 그 경우에는 더 탐색할 필요없이 나눠주면 동전의 수가 나옴
  elif (K/coin[coinFinder]>=1):
    if (K%coin[coinFinder]==0):
      bill+=int(K/coin[coinFinder])
      K=K%coin[coinFinder]
      break

  bill+=int(K/coin[coinFinder])
  K=K%coin[coinFinder]
  coinFinder+=1
  

print(bill)


#way-1
# coinFinder = 0
# bill = 0

# while 0 != K:

#   if coin[coinFinder] < K:
#   # 마지막 인덱스까지 갔는데, 더큰 동전이없다면 거기서 바로빼버리고 다시 탐색
#     if (coinFinder==N-1):
#       K=K-coin[coinFinder]
#       bill+=1
#       coinFinder=0
#       continue
#   # 작은 단위의 동전부터 차례로 비교, 기준 비용보다 작다면 다음 인덱스로 이동
#     coinFinder += 1
#     continue
#   # 기준 비용보다 동전이 더 크다면, 해당 인덱스보다 1적은 인덱스로 이동하여 값을 빼고, 다시 인덱스 0부터 탐색하기시작
#   elif coin[coinFinder] > K:
#     K = K-coin[coinFinder-1]
#     bill += 1
#     coinFinder = 0
#   # 같다면 빼고 종료
#   elif (coin[coinFinder] == K):
#     bill += 1
#     break

# print(bill)
