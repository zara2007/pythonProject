a,b = map(int,input().split())
sum = 0
for i in range (a,b+1):
    sum = sum + i**2
print(sum)