n = int(input())
k = 1
sum = 0
for i in range(1, n + 1):
    sum += k
    k += 2
print(sum)
