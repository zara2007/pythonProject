a,n = map(int,input().split())
sum = 1
for i in range (1,n+1):
    sum+=a**i
print(sum)