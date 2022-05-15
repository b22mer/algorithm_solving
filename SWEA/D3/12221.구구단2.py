T= int(input())
for i in range(T):
    first,second=map(int,input().split())
    result=0
    if (first>=10 or second>=10 ):
        result=-1
    else:
        result=first*second
    
    print("#{} {}".format(i+1, result))