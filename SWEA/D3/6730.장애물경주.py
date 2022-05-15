# 파이썬 언어지원 안함

testcase = int(input())

for i in range(testcase):

    heightCase = int(input())

    testHeight = list(map(int, input().split()))
    min = 0
    max = 0

    for j in range(heightCase-1):
        if (testHeight[j+1]-testHeight[j]) >= 0:
            if max < testHeight[j+1]-testHeight[j]:
                max = testHeight[j+1]-testHeight[j]
                
        elif (testHeight[j+1]-testHeight[j]) < 0:
            if min > testHeight[j+1]-testHeight[j]:
                min = testHeight[j+1]-testHeight[j]

    print("#",end="")
    print(i+1,max, abs(min))
