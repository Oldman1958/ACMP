n = input()
count = 0
for i in n:
    if i == '0' or i == '6' or i == '9':
        count += 1
    elif i == '8':
        count += 2
    else:
        continue
print(count)

