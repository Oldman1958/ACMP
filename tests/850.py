a, b = map(int, input().split())
minimal = 0
maximal = 0
if (min(a, b) // 2) + (min(a, b) % 2) == (max(a, b) // 2) + (max(a, b) % 2):
    minimal = (min(a, b) // 2) + (min(a, b) % 2)

else:
    minimal = (max(a, b) // 2) + (max(a, b) % 2)
maximal = min(a, b)
print(minimal, maximal)
