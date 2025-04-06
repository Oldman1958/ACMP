n = int(input())
out = bin(n)
count = 0
for i in out:
    if i == '1':
        count += 1
print(count)