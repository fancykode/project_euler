NUM = 1000

# calculate triangle number
def tnum(n):
    return (n * (n + 1)) // 2


# 3 * ( 1 + 2 + 3 + 4 + ... ) + 5 * (1 + 2 + 3 + ...) - 15*(1 + 2 + 3 + ...)

a = tnum((NUM - 1) // 3)
b = tnum((NUM - 1) // 5)
c = tnum((NUM - 1) // 15)

print(3 * a + 5 * b - 15 * c)
