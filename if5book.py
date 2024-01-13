a, b, c = map(int, input().split())
count = 0
coount = 0
if a > 0 and b > 0 and c > 0:
    count = 3
elif a < 0 and b < 0 and c < 0:
    coount = 3
elif a > 0:
    count += 1
    coount += 2
    if b > 0 and c < 0:
        count += 1
        coount -= 1
    elif b < 0 and c > 0:
        count += 1
        coount -= 1
elif b > 0:
    count += 1
    coount += 2
    if a > 0 and c < 0:
        count += 1
        coount -= 1
    elif a < 0 and c > 0:
        count += 1
        coount -= 1
print(count)
print(coount)
