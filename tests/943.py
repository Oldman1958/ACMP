n, m, y, x = map(int, input().split())
z = []
cell = 0
for i in range(n):
    row = []
    z.append(row)
    for j in range(m):
        row.append(cell)
        cell += 1
for i in range(n):
    if i % 2 != 0:
        z[i].reverse()
print(z[y - 1][x - 1])

