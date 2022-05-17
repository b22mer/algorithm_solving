TC=int(input())
for i in range(TC):
  A,B,C = map(int, input().split())
  selectBread=min([A,B])
  maxBread=C//selectBread
  print("#{} {}".format(i+1, maxBread))