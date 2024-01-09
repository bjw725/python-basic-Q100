# 거스름돈 가장 적게 주기
n = 1260
cnt = 0

coin_types=[500, 100, 50, 10]

for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)

