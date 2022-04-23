
testcase = int(input())
sum = 0
sumTotal = []

for i in range(testcase):
    ALen, BLen = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxNum = []
    if (len(A) == len(B)):
        for j in range(len(A)):
            sum += A[j]*B[j]
        maxNum.append(sum)
    elif (len(A) > len(B)):
        for j in range(len(A)-len(B)+1):
            for k in range(len(B)):
                sum += B[k]*A[j+k]
            maxNum.append(sum)
            sum=0
    elif (len(B) > len(A)):
        for j in range(len(B)-len(A)+1): 
            for k in range(len(A)):
                sum += A[k]*B[j+k]
            maxNum.append(sum)
            sum=0
    sumTotal.append(max(maxNum))

for i in range(testcase):
    print("#", end="")
    print(i+1, sumTotal[i])

