

from traceback import print_tb


testcase = int(input())

result = 0
for i in range(8):
    testX = [0 for j in range(8)]
    testX[i] = list(input())

    # 가로줄 테스트

    for j in range(8-testcase+1):
        cnt = 0
        for k in range(testcase//2):
            if testX[i][k+j] == testX[i][j+testcase-1-k]:
                cnt += 1
        if cnt == testcase//2:
            result += 1

    rotateX=testX
    print(rotateX)
    for x in range(8):
        for y in range(8):
            rotateX[y][8-1-x]=testX[x][y]
    
print("로테이트", rotateX)
    