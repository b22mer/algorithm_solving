
N= int(input())

A=[0 for i in range(N)]
B=[0 for i in range(N)]

A=list(map(int, input().split()))
B=list(map(int, input().split()))


sumOfaAndb=0

A.sort()
B.sort()
B.reverse()


i=0
while i<N:
  sumOfaAndb+=A[i]*B[i]
  i+=1

print(sumOfaAndb)