SUM = 1000

def find_triplet():
    for a in range(1, SUM):
        for b in range(a + 1, SUM):
            c = SUM - a - b
            if a < b and b < c and a * a + b * b == c * c:
                return (a, b, c)

t = find_triplet()
print(t[0] * t[1] * t[2])
