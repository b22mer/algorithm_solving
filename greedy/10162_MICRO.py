# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초 저장
# 냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다. 
# 우리는 A, B, C 3개의 버튼을 적절히 눌러서 그 시간의 합이 정확히 T초가 되도록 해야 한다. 
# 단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다. 이것을 최소버튼 조작이라고 한다. 
# 20220323

inputTime= int(input())


t_300=0
t_60=0
t_10=0

while (inputTime%300!=0 and inputTime>=0) and (inputTime%60!=0 and inputTime>=0):
  t_10+=1
  inputTime=inputTime-10

while (inputTime%300!=0 and inputTime>=0):
  t_60+=1
  inputTime=inputTime-60

if inputTime<0:
  print(-1)
else:
  t_300=int(inputTime/300)
  print(t_300,t_60,t_10)

