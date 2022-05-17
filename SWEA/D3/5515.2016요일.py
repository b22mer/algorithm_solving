T=int(input())
for i in range(T):
  month, day= map(int,input().split())
  monthList=[4,5,6,0,1,2,3]
  monthDays=[31,29,31,30,31,30,31,31,30,31,30,31]

  totalDay=sum(monthDays[:month-1])+day
  monthSelect=monthList[totalDay%7-1]

  print("#{} {}".format(i+1, monthSelect))