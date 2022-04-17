
T = int(input())
payBill = [0 for i in range(T)]
totaltoken = []

cash = 0
for i in range(T):
    cash = int(input())  # split로 입력하면 배열의 형태로 입력이된다.
    payBill[i] = cash


for i in range(T):

    token_25 = payBill[i]//25
    payBill[i] = payBill[i] % 25

    token_10 = payBill[i]//10
    payBill[i] = payBill[i] % 10

    token_5 = payBill[i]//5
    payBill[i] = payBill[i] % 5

    token_1 = payBill[i]//1

    totaltoken.append([token_25, token_10, token_5, token_1])

s = 0
for i in range(T):
    print(' '.join(map(str, totaltoken[i])))
    # 정수 리스트를 공백으로 출력하는 메커니즘
    # 문자열은 ' '.join(list) 이런식으로 가능
