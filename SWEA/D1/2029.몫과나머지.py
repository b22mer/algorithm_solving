
n=int(input())

result=[]


for i in range(n):
  first,second=map(int,input().split())
  mok=first//second
  nameoge=first%second
  result.append([mok,nameoge])
  

for i in range(n):
  print("#",end="")
  print(i+1, " ".join(map(str,result[i])))
