T=int(input())
for i in range(T):
    testCase=list(input())

    testCase.reverse()
    for j in range(len(testCase)):
        if testCase[j]=='b':
            testCase[j]='d'
        elif testCase[j]=='p':
            testCase[j]='q'
        elif testCase[j]=='q':
            testCase[j]='p'
        elif testCase[j]=='d':
            testCase[j]='b'
    print("#{} {}".format(i+1,"".join(testCase)))