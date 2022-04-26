

testcase=int(input())

for tc in range(testcase):
  N,K=map(int, input().split())

  resultCase=[list(map(int,input().split())) for _ in range(N)]
  total=0
  for i in range(N):
    cnt=0
    for j in range(N):
      if resultCase[i][j]==1:
        cnt+=1
      if resultCase[i][j]==0 or j==N-1:
        if cnt==K:
          total+=1
        cnt=0


    for j in range(N):
      if resultCase[j][i]==1:
        cnt+=1
      if resultCase[j][i]==0 or j==N-1:
        if cnt==K:
          total+=1
        cnt=0

  print("#{} {}".format(tc+1,total))



#   for x in range(N):
#     cnt=0
#     for y in range(N-1):
#       if testCoor[y][x]==0 and testCoor[y][x]==testCoor[y+1][x]:
#         cnt+=1
#     if cnt==1:
#       sum+=1

#   resultCase.append(cnt)

# print(resultCase) 0 0 1 1 0

