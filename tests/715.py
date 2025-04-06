n, m = map(int, input().split())
neg = []
pos = []
count = 0
for i in range(n):
    neg.append(input())
input()
for i in range(n):
    pos.append(input())
for i in range(n):
    for j in range(m):
        if neg[i][j:j + 1] == pos[i][j:j + 1]:
            count += 1
print(count)
