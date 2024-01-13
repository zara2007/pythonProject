array= []
for i in range(3):
    array.append(int(input()))
k = 1
for i in range(3):
    k = k * array[i]
print(k)