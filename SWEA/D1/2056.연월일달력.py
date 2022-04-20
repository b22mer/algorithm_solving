



N = int(input())

date = [0 for i in range(N)]
result = []

for i in range(N):
    date[i] = input()

    year = date[i][0:4]
    month = date[i][4:6]
    day = date[i][6:8]
    if (int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1):
        result.append(-1)
    elif (int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11):
        if (int(day) >= 31):
            result.append(-1)
        else:
            result.append(year+"/"+month+"/"+day)
    elif (int(month) == 2):
        if (int(day) > 28):
            result.append(-1)
        else:
            result.append(year+"/"+month+"/"+day)

    else:
        if (int(day) > 31):
            result.append(-1)
        else:
            result.append(year+"/"+month+"/"+day)

for i in range(N):
    print("#",end="")
    print(i+1,result[i])
