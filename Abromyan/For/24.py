x, n = map(int, input().split())
sum = 1
k = 1
f = 1
for i in range(1 ,n + 1):
    f *= 2*i
    sum += ((-1 ** i) * x ** (2*i)) / f
print(sum)
