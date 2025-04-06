s = input() + '1'
count = 0
count_max = 0

for i in s:
    if int(i) == 0:
        count += 1

    elif i != 0:
        if count > count_max:
            count_max = count
        count = 0
print(count_max)

