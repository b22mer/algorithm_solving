# ord("A")
# chr(76)


test = input()
result = []
for i in range(len(test)):
    result.append(ord(test[i])-64)


print(' '.join(map(str, result))) 
# join은 정수는 적용이 되지않는다.
# 문자열로 변환한후 사용한다.
