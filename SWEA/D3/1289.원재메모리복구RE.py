testcase = int(input())

for i in range(testcase):
    testBinary = input()

    binaryLen = len(testBinary)
    flag = "0"
    cnt = 0

    for j in range(binaryLen):
        if testBinary[j]!=flag:
            cnt+=1
            if flag=="0":
                flag="1"
            else:
                flag="0"
    print("#{} {}".format(i+1, cnt))
