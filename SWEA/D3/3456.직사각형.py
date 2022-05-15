T=int(input())
for i in range(T):
    a,b,c=map(int, input().split())
    resultlen=0
    if (a==b and b==c):
        resultlen=a
    elif (a==b and b!=c ):
        resultlen=c
    elif (a!=b and b!=c):
        resultlen=b
    elif (a!=b and b==c):
        resultlen=a
    print("#{} {}".format(i+1,resultlen))