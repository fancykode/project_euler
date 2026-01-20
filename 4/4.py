palindromes = set()
for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        n = a * b
        n_str = str(n)
        n_str_rev = n_str[::-1]
        if n_str == n_str_rev:
            palindromes.add(n)
print(max(palindromes))
