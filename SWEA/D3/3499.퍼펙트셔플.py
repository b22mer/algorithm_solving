T=int(input())
for i in range(T):
  kardNum=int(input())
  kardList=input().split()
  newList=[]
  if (kardNum%2==0):
    divideA=kardList[0:len(kardList)//2]
    divideB=kardList[len(kardList)//2:]

    for j in range(kardNum//2):
      newList.append(divideA[j])
      newList.append(divideB[j])

  else:
    divideA=kardList[0:len(kardList)//2+1]
    divideB=kardList[len(kardList)//2+1:]

    for j in range(kardNum//2):
      newList.append(divideA[j])
      newList.append(divideB[j])
    newList.append(divideA[-1])

  print("#{} {}".format(i+1, " ".join(newList)))