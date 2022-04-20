
N = int(input())
num = [0 for i in range(N)]
total = []
average = []
for i in range(N):

    num[i] = list(map(int, input().split()))
    total.append(sum(num[i]))

    average.append(round(total[i]/10))
    # 소수 첫째자리에서 반올림하는 부분


for i in range(N):
    print("#", end="")
    print(i+1, average[i])
