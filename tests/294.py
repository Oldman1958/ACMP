k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())
k1_ost = k1 - int((k1 * l1) / 100)
k2_ost = k2 - int((k2 * l2) / 100)
utr = 0
if k1_ost < k2_ost:
    utr = (k1 - k1_ost) * m1 + (k2 - k1_ost) * m2
else:
    utr = (k2 - k2_ost) * m2 + (k1 - k2_ost) * m1
print(utr)
