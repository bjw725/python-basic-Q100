# 1이 될 때 까지
a, b = map(int, input().split())
cnt = 0
while True:
    for i in range(a):
        if a == 1:
            break
        elif a % b == 0:
            a /= b
            cnt += 1
        else:
            a -= 1
            cnt += 1
    if a == 1:
        break
print(cnt)