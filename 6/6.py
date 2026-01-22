N = 100

sum_of_sq = 0
sq_of_sum = 0
for i in range(1, N + 1):
    sum_of_sq += i * i
    sq_of_sum += i
sq_of_sum *= sq_of_sum
diff = abs(sum_of_sq - sq_of_sum)
print(diff)
