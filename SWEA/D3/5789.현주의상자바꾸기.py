T = int ( input())
for i in range(T):
  N,Q=map(int,input().split())
  testList=[0 for i in range(N)]
  for j in range(1,Q+1):
    L,R= map(int,input().split())
    for k in range(L,R+1):
      testList[k-1]=j
  
  print("#{} {}".format(i+1, " ".join(map(str,testList))))




