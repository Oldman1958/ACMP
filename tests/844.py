a, b = map(int, input().split())
"""
if ((a * b) ** 0.5) % 1 == 0:
    print(int((a * b) ** 0.5))
else:
    print('0')
"""
print(int((a * b) ** 0.5) if ((a * b) ** 0.5) % 1 == 0 else '0')
