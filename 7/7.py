import math

PRIME_NUM_INDEX = 10_001

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

n = 2
i = 1
while True:
    if is_prime(n):
        if i == PRIME_NUM_INDEX:
            break
        i += 1
    n += 1
print(n)
