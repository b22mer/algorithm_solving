T = int(input())
for i in range(T):
    # n은 뿔의 개수, m은 마리수
    n, m = map(int, input().split())
    twinNum = n-m
    uniconNum = m-twinNum
    print("#{} {} {}".format(i+1, uniconNum, twinNum))
