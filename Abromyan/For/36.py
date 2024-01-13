k,n = map(int,input().split())
sum = 0
for i in range(1,n+1):
    sum = sum + i**k
print(sum)
