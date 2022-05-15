testcase = int(input())

for i in range(testcase):
    firstHour, secondHour = map(int, input().split())
    totalHour = (firstHour+secondHour) % 24

    print("#{} {}".format(i+1, totalHour))
