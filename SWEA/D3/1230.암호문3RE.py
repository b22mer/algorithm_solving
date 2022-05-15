for _ in range(10):
    testLen = int(input())
    testList = list(map(int, input().split()))
    cmdNum = int(input())
    cmd = input().split()
    cmdLen = len(cmd)

    for i in range(cmdLen):

        if cmd[i] == 'I':
            x=int(cmd[i+1])
            y=int(cmd[i+2])
            for j in range(y):
                testList.insert(x, cmd[i+3+j])
                

        elif cmd[i] == 'D':
            x=int(cmd[i+1])
            y=int(cmd[i+2])
            
            for j in range(y):
                del testList[x+j]
                

        elif cmd[i] == 'A':
            y = int(cmd[i+1])
            for j in range(1, y+1):
                testList.append(int(cmd[i+1+j]))
    print(testList)

