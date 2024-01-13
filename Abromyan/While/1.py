a,b = map(int,input().split())
i = 1
while b * i < a:
    i += 1
else:
    print(a - (b * (i - 1)))