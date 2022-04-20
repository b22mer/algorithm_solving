#3 2 4 18 15 28


N=int(input())

# 입력받은 길이 만큼 배열에 0을 넣어준다.
rope=[0 for i in range(N)]
 
i=0
# 입력 받은 길이만큼 원하는 숫자들을 줄 단위로 넣어준다.
while i <N:
  elements=int(input())
  rope[i]=elements
  i+=1

# 입력받은 배열을 정렬해줌으로써 작은 숫자가 순서로 앞에서부터 정렬되도록한다.
rope.sort()

j=0
maxWeight=0

# 최대의 숫자를 찾기위해서 처음부터 검사해가면서 최대의 무게를 찾아낸다. 
# 몇개를 쓰는지는 따로 나타낼 필요가 없기때문에 무게를 구하는데 치중한다.
while j<N: 
  selectNum=rope[j]*(N-j)
  if (selectNum>maxWeight):
    maxWeight=selectNum
  j+=1
  

print(maxWeight)