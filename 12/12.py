import math


def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2

        # n is odd here
    for i in range(3, math.isqrt(n) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors


i = 1
tnum = 0
while True:
    tnum += i
    i += 1
    factors = prime_factors(tnum)

    divisors = 1
    for exp in factors.values():
        divisors *= exp + 1
    if divisors > 500:
        print(tnum)
        break
