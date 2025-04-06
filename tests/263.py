n, a, b = map(int, input().split())
if a > b:
    a1 = b + (n - a) - 1
else:
    a1 = a + (n - b) - 1
a = abs(a - b)
print(a1 if a1 < a else a - 1)
