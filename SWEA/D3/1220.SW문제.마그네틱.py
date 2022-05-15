
def list_chuck(arr, n):
    return [arr[i: i + n] for i in range(0, len(arr), n)]

for i in range(1):

  testLen=int(input())
  testlist=list(map(int,input().split()))
  result_list=list_chuck(testlist, 100)
  print(result_list)

  cnt=0
  for j in range(100):
    flag=0
    for k in range(100):
      if result_list[k][j]==1 and flag==0:
        flag=1
    
      if result_list[k][j]==2 and flag==1:
        cnt+=1
        flag=0
  print(cnt)
    




