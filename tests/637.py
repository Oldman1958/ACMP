n = int(input())
team = list(map(int, input().split()))
k = int(input())
ans = 0
for i in range(n):
    ans = ans + min(team[i], k)
print(ans)
