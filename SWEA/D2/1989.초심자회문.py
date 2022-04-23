testcase = int(input())
testText = 0
resultCase = []
for i in range(testcase):

    testText = input()
    cnt = 0
    a = (len(testText))//2
    for j in range(a):
      if (testText[j] != testText[len(testText)-1-j]):
            cnt += 1
      else:
            cnt += 0
            
    if cnt == 0:
      resultCase.append(1)
    elif cnt>=1:
      resultCase.append(0)

for i in range(len(resultCase)):
    print("#",end="")
    print(i+1,resultCase[i])
