
def power (a,b):
    if b==0:
        return 1;
    
    return a*power(a, b-1)



for i in range(10):
    number=int(input())
    firstNum, secondNum= map(int,input().split())
    
    
    print("#{} {}".format(number,power(firstNum,secondNum)))