N = 4000000

prev = 2
prev_prev = 1

ans = 2
while True:
    cur = prev + prev_prev
    if cur >= N:
        break
    if cur % 2 == 0:
        ans += cur
    prev_prev = prev
    prev = cur
print(ans)
