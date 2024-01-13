d = 0
sum = 0
for i in range (9999999999):
    a = int(input())
    if a == 0:
        break
    d += 1
    sum +=a
print(sum/d)