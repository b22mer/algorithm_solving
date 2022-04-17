

N = int(input())
debate = []

for i in range(N):
    first, second = map(int, input().split())  # 줄 단위로 공백기준으로 입력을 받는 구간
    debate.append([first, second])
debate.sort(key=lambda x: x[0])  # 리스트안 리스트에서 첫번째 인자기준으로 정렬
debate.sort(key=lambda x: x[1])  # 리스트안 리스트에서 두번째 인자기준으로 정렬

last = 0
cnt = 0

for i, j in debate:
    if i >= last:
        cnt += 1
        last = j
print(cnt)

# 처음엔 시작시간기준으로 정렬 진행, 두번째는 종료시간 기준으로 진행
