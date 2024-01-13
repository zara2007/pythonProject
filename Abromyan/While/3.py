n, k = map(int, input().split())
sum = 0
i = 0
while n - sum > k:
    sum += k
    if sum > n:
        break
    i += 1
print(i)
print(sum)
print(n - sum)