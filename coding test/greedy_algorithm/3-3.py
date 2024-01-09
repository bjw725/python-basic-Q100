# 숫자 카드 게임
a, b = map(int, input().split())
result = 0
for i in range(a):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
