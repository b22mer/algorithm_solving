n = int(input())
num = [0 for i in range(n)]
result = []
re_result = []
for i in range(n):

  test = int(input())
  source = [0 for i in range(test)]
  source[i] = input().split()
  result.append(source[i])
  re_result.append( list(map(int, result[i])))


for i in range(n):

  re_result[i]