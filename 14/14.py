mem = {}


def gen_collatz(val):
    count = 1
    n = val
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n in mem:
            mem[val] = mem[n] + count
            return mem[val]
        count += 1
    mem[val] = count
    return mem[val]


max_len = 0
start_num = -1
for i in range(1, 1000000):
    len = gen_collatz(i)
    if len > max_len:
        max_len = len
        start_num = i

print(start_num, max_len)
