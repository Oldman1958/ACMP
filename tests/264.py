n = int(input())
tmp_max = 0
count = 0
count_max = 0
tmp = list(map(int, input().split()))
# print(tmp)
for i in range(n):
    if tmp[i] <= 0:
        count = 0
    else:
        count += 1
        if count > count_max:
            count_max = count
print(count_max)
