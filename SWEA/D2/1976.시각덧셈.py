
testcase=int(input())

for i in range(testcase):

  firstHour, firstMinute,secondHour, secondMinute= map(int, input().split())

  finalMinute=firstMinute+secondMinute
  finalHour=firstHour+secondHour

  if finalMinute>=60:
    finalMinute=finalMinute%60
    finalHour+=1
  
  if finalHour>12:
    if (finalHour==24):
      finalHour=12
    else: finalHour=finalHour%12

  print("#{} {} {}".format(i+1, finalHour, finalMinute))
  
  