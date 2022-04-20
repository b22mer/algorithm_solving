
from cgi import print_arguments


N= input()

# 1020 -> 2100

if (N.find("0")==-1):
  print(-1)

elif N=="30":
  print(N)
else:
  findMax=list(N)
  findMax.sort()
  findMax.reverse()
  findMax.pop()
  refresh="".join(findMax)
  refreshMax=int(refresh)%3
  if (refreshMax!=0):
    print(-1)
  else:
   answer= refresh+"0"
   print(answer)



