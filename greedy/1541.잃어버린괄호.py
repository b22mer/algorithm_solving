a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

# tip 최소를 만들기 위해서는 "-"단위로 나누면 된다.
# int()는 0009 같은 숫자를 처리해준다.