
test = int(input())
num = []
result = (test+1)//2 - 1
num = list(map(int, input().split()))
num.sort()
# sort만 하고도 그냥 실행이된다.

print(num[result])
