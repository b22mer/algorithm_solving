
testcase=int(input())

for i in range(testcase):
  
  person=int(input())
  personDistance=list(map(int,input().split()))

  for j in range(person):
    personDistance[j]=abs(personDistance[j])
  
  minDistance=min(personDistance)
  minChances=personDistance.count(minDistance)

  print("#{} {} {}".format(i+1,minDistance,minChances ) )

