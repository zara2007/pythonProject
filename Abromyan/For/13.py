n = int(input())
sum = 0
a = 1.1
for i in range(1, n + 1):
    sum += (1 + i * 0.1) * (-1) ** (i + 1)
print(sum)
