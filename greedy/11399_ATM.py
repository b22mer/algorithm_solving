
#Way1

N=int(input())

P=[0 for i in range(N)]
i=0


P=list(map(int, input().split()))
# *반복문이 아닌 map 함수를 통해서 한줄에 입력값들을 받았어야했다.
P.sort()

j=0
total=0

while j<N:
  total+=sum(P[0:j+1])
  j+=1


print(total)
  

# point! 한줄에 공백을 기준으로 입력 받는가? 여러줄에 하나씩 받는가 구분해야한다.