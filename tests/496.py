n = int(input())
r = list(map(int, input().split()))
count = 0
count_max = 0
r.append(r[0])
r.append(r[1])
for i in range(n):
    if i == 0:
        count = r[0] + r[n - 1] + r[n - 2]
    elif i == 1:
        count = r[0] + r[1] + r[n - 1]
    else:
        count = r[i - 1] + r[i] + r[i + 1]
    if count > count_max:
        count_max = count
print(count_max)
