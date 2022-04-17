from pickletools import read_uint1


city = int(input())

lenOfCity = [0 for i in range(city-1)]
priceOfCity = [0 for i in range(city)]

lenOfCity = list(map(int, input().split()))
priceOfCity = list(map(int, input().split()))

result = 0

if priceOfCity[0] == min(priceOfCity):
    result = sum(lenOfCity)*priceOfCity[0]
    print(result)
    # 보류
# 일단 처음인덱스 기준으로 앞 인덱스의 인자들이
# 큰지 안큰지 비교한다음에 크다면 미리 사들임
