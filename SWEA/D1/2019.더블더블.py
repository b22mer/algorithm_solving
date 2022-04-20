n=int(input())

result=1
num=[]
for i in range(n+1):

  if (i==0):
    num.append(1)
  else:
    result=result*2
    num.append(result)
  

print(' '.join(map(str,num)))
