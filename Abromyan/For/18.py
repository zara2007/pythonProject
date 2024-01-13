a,n = map(int,input().split())
sum = 0
for i in range (0, n + 1):
    sum += (a ** i) * ((-1) ** i)
print(sum)