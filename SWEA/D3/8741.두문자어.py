testcase=int(input())
for i in range(testcase):
  first, second, third=input().split()
  firstRe=first[0].upper()
  secondRe=second[0].upper()
  thirdRe=third[0].upper()
  result=firstRe+secondRe+thirdRe
  print("#{} {}".format(i+1, result))