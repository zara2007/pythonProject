a,b,c = map(int,input().split())
count = 0
if a > 0 and b > 0 and c > 0:
    count = 3
elif a > 0:
    count += 1
    if b > 0 and c < 0:
        count += 1
    elif b < 0 and c > 0:
        count += 1
elif b > 0:
    count += 1
    if a > 0 and c < 0:
        count += 1
    elif a < 0 and c > 0:
        count += 1
elif c > 0:
    count += 1
    if a > 0 and b < 0:
        count += 1
    elif a < 0 and b > 0:
        count +=1

print(count)