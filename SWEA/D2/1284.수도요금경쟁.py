# A사는 리터당 P원
# B사는 기본요금 Q if R리터이하이면/ 넘으면 초과랑만큼 S원 추가

testcase=int(input())
result_list=[]

for i in range(testcase):
  A=0
  B=0
  result=0
  P,Q,R,S,W=map(int,input().split())

  A=P*W

  if W>R:
    B=Q+(W-R)*S
  else:
    B=Q

  if(A>B):
    result_list.append(B)
  else:
    result_list.append(A)

for i in range(testcase):
  print("#",end="")
  print(i+1, result_list[i])