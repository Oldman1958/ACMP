n = int(input())
k = ['No'] * n
for i in range(n):
    s = input()
    s1 = sum(map(int, s[:3]))
    s2 = sum(map(int, str(int(s[3:]) + 1)))
    s3 = sum(map(int, str(int(s[3:]) - 1)))
    if s1 == s2 or s1 == s3:
        k[i] = 'Yes'
for i in k:
    print(i)
