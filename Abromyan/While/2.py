a,b = map(int,input().split())
i = 1
res = 0
while b * i < a:
    i += 1
    res = i
print(res-1)