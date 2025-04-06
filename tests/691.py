import re

n = int(input())
number = []
for i in range(n):
    number.append(input())
for i in range(n):
    if len(number[i]) == 6 and re.fullmatch("([ABCEHKMOPTXY])(\d{3})([ABCEHKMOPTXY]{2})", number[i]):
        print("Yes")
    else:
        print("No")
