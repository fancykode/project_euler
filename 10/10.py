N = 2_000_000

primes = [True for _ in range(0, N + 1)]

primes[0] = False
primes[1] = False

for i in range(2, len(primes)):
    if primes[i]:
        for j in range(i * i, len(primes), i):
            primes[j] = False


ans = 0
for i in range(0, len(primes)):
    if primes[i]:
        ans += i
print(ans)
