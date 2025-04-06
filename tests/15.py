n = int(input())
m = []
for row in range(n):
    m.append(list(map(int, input().split())))
k = 0
for i in range(1, n):
    for j in range(i + 1):
        k += m[i][j] == 1
print(k)
