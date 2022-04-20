# 가능한 수의 최댓값과 최솟값을 찾아라!



firstNum,secondNum= input().split(' ')

minFirstNum=firstNum
minSecondNum=secondNum



min=0
max=0

i=0
indexFinder_1=0

# print(type(firstNum.find("5")))

while (firstNum.find("5")!=-1):
  indexFinder_1=firstNum.find("5",indexFinder_1,len(firstNum)-1)
  tmp=list(firstNum)
  tmp[indexFinder_1]="6"
  firstNum="".join(tmp)

indexFinder_2=0
while (secondNum.find("5")!=-1):
  indexFinder_2=secondNum.find("5",indexFinder_2,len(secondNum)-1)
  tmp=list(secondNum)
  tmp[indexFinder_2]="6"
  secondNum="".join(tmp)


indexFinder_1=0
while (minFirstNum.find("6")!=-1):
  indexFinder_1=minFirstNum.find("6",indexFinder_1,len(minFirstNum)-1)
  tmp=list(minFirstNum)
  tmp[indexFinder_1]="5"
  minFirstNum="".join(tmp)

indexFinder_2=0
while (minSecondNum.find("6")!=-1):
  indexFinder_2=minSecondNum.find("6",indexFinder_2,len(minSecondNum)-1)
  tmp=list(minSecondNum)
  tmp[indexFinder_2]="5"
  minSecondNum="".join(tmp)



firstNum= int(firstNum)
secondNum=int(secondNum)
minFirstNum=int(minFirstNum)
minSecondNum=int(minSecondNum)


print( minFirstNum+minSecondNum,firstNum+secondNum)
