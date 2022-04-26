
testcase = int(input())
totalDate = []
total_minus=[]
for i in range(testcase):
  totlaDateLen=[0,0]
  totalDate.append(list(map(int, input().split())))


  for j in range(2):
    
    if totalDate[i][2*j] == 1: totlaDateLen[j] += totalDate[i][2*j+1]
    if totalDate[i][2*j] == 2: totlaDateLen[j] += totalDate[i][2*j+1]+31
    if totalDate[i][2*j] == 3: totlaDateLen[j] += totalDate[i][2*j+1]+31+28
    if totalDate[i][2*j] == 4: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31
    if totalDate[i][2*j] == 5: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30
    if totalDate[i][2*j] == 6: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31
    if totalDate[i][2*j] == 7: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31+30
    if totalDate[i][2*j] == 8: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31+30+31
    if totalDate[i][2*j] == 9: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31+30+31+31
    if totalDate[i][2*j] == 10: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31+30+31+31+30
    if totalDate[i][2*j] == 11: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31+30+31+31+30+31
    if totalDate[i][2*j] == 12: totlaDateLen[j] += totalDate[i][2*j+1]+31+28+31+30+31+30+31+31+30+31+30

  total_minus.append(abs(totlaDateLen[0]-totlaDateLen[1])+1)


for i in range(testcase):
    print("#", end="")
    print(i+1, total_minus[i])

