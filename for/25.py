a = 0
k = 1
for i in range(999999999):
    d = float(input())
    if d == 0:
        break
    a+=1
    k = k*d
print(k)