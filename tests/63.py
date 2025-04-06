"""
read(s,p);
for x=1..30000{
  y=s-x;
  if(x<=y и x*y==p) write(x,' ',y);
}

x, y = map(int, input().split())
s = x + y
p = x * y
print(s, p)
for x in range(1, 1000):
    y = s - x
    if x <= y and x * y == p:
        print(x, y)
"""
s, p = map(int, input().split())
x = (s + (s * s - 4 * p) ** 0.5) / 2
print(int(min(x, s - x)), int(max(x, s - x)))
