T= int(input())
for i in range(T):
  N=int(input())
  results=0
  for j in range(N):
    p,a=map(float, input().split())
    results+=p*a
  f=format(results,"0.6f")

  print("#{} {}".format(i+1,f))


