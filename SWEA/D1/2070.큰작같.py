
test= int(input())
set= [0 for i in range(test)]
result=[]

for i in range(test):
    set[i]=list(map(int,input().split()))
    
    if (set[i][0] ==set[i][1]):
        result.append("=")
    elif (set[i][0] <set[i][1]):
        result.append("<")
    else:
        result.append(">")

for i in range(test):
    print("#",end="")
    print(i+1, result[i])
        
    