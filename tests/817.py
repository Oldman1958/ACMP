n, m, d, k = map(int, input().split())
S_s = m * d * k
S_a = n * d * k
count = n * m
S_p = (d ** 2) * count
S = S_s + S_a - S_p
print(S)
