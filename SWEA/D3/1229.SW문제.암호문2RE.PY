for i in range(10):
    pwLen = int(input())
    originList = list(map(int, input().split()))
    cmdNum = int(input())
    cmdList = input().split()
    cmdLen = len(cmdList)
    chk = 0
    while chk < cmdNum:
        for j in range(cmdLen):
            if cmdList[j] == "I":
                x = int(cmdList[j+1])
                for k in range(int(cmdList[j+2])):
                    originList.insert(x, int(cmdList[j+3+k]))
                chk += 1
            elif cmdList[j] == "D":
                x = int(cmdList[j+1])
                for z in range(int(cmdList[j+2])):
                  del originList[x]
                chk+=1
    originList = list(map(str, originList))
    print("#{} {}".format(i+1, " ".join(originList)))
    # 맞은거라고 침
