a = 0
sum = 0
for i in range(99999999):
    d = int(input())
    if d == 0 and d%2==0:
        break
    a+=1
    sum +=a
print(sum)
