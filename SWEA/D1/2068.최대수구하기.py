
from cgitb import reset
from unittest import result


test=int (input())

testList=[0 for i in range(test)]
result=[]
for i in range(test):
    testList[i]=list(map(int,input().split()))
    result.append(max(testList[i]))
    
for i in range(test):
    print("#",end="")
    print(i+1, result[i])