import math

N = 600851475143

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # n is odd here
    for i in range(3, math.isqrt(n) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

print(max(prime_factors(N)))
