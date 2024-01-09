# 완전 탐색 유형
# 시각 (23시 59분 59초) 안에 3이 포함된 경우의 수
# 하루는 86400초로, 00시00분00초부터 23시 59분 59초까지의 모든 경우는 86400가지밖에 존재하지 않기 때문에 100,000개도 되지 않으므로 문자열 연산을 이용해 3이 시각에 포함되어 있는지 확인
h = int(input())

cnt = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
