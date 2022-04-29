
testcase= int(input())

for i in range(testcase):

  N,K=map(int,input().split())
  result=0
  students=[0 for i in range(N)]
  
  for j in range(N):
    midterm, final, homework=map(int, input().split())
    total=midterm+ final+ homework
    students[j]=total

  Kstudent=students[K-1]
  students.sort(reverse=True)

  KstudentNum=students.index(Kstudent)+1

  if 0.1>=(KstudentNum/N):
    result="A+"
  elif 0.2>=(KstudentNum/N):
    result="A0"
  elif 0.3>=(KstudentNum/N):
    result="A-"
  elif 0.4>=(KstudentNum/N):
    result="B+"
  elif 0.5>=(KstudentNum/N):
    result="B0"
  elif 0.6>=(KstudentNum/N):
    result="B-"
  elif 0.7>=(KstudentNum/N):
    result="C+"
  elif 0.8>=(KstudentNum/N):
    result="C0"
  elif 0.9>=(KstudentNum/N):
    result="C-"
  elif 1.0>=(KstudentNum/N):
    result="D0"

  print("#{} {}".format(i+1, result) )

