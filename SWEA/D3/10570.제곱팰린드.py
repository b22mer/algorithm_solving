import math


testcase = int(input())


for j in range(testcase):
    A, B = input().split()
    cnt = 0
    for i in range(int(A), int(B)+1):
        testStr = str(i)
        testSq= str(int(math.sqrt(int(i))))

        if 0 < i and i < 10 and math.sqrt(int(i)) % 1 == 0:
            cnt += 1
        elif (testSq[0]==testSq[-1]) and math.sqrt(int(i)) % 1 == 0 and testStr[0] == testStr[-1]:
            cnt += 1

    print("#{} {}".format(j+1, cnt))
