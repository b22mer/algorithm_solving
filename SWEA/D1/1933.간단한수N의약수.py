
n=int(input())
cnt=0
num=[]
for i in range(n):

  if (n%(i+1)==0):
    num.append(i+1)

print(' '.join(map(str,num)))

