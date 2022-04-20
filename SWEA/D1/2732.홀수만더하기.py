
N = int(input())
num = [0 for i in range(N)]
# 0으로 초기화

total = []

for i in range(N):

    num[i] = list(map(int, input().split()))
    # num을 2차원 배열로
    my = []
    for j in range(10):
        if (num[i][j] % 2 != 0):
            my.append(num[i][j])
            # 인자가 홀수인지 걸러주는 장치
    total.append(sum(my))


for i in range(N):
    print("#", end="")
    print(i+1, total[i])
