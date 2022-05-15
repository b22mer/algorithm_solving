testcase = int(input())

for i in range(testcase):
    setDeg = int(input())

    # 1도당 2분
    # 30도당 1시간

    resultHour = setDeg//30
    sourceMinute = setDeg % 30
    resultMinute=sourceMinute*2
    
    print("#{} {} {}".format(i+1,resultHour,resultMinute))
