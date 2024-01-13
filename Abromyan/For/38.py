n = int(input())
sum = 0
a = 1
for i in range (n,1,-1):
    a+=1
    sum = sum + a**i
print(sum)