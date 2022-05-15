T=int(input())
for i in range(T):
    peopleNum, p, t = map(int, input().split())
    maxi=min([p,t])
    
    if (p+t)<peopleNum:
        mini=0
    else:
        mini=(p+t)-peopleNum
    
    print("#{} {} {}".format(i+1, maxi,mini))
