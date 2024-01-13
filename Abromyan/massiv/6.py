array = []
n = int(input())
sum = 1


for i in range(n):
    print((array[i])%1, end=" ")
    sum = sum * (array[i])%1
print(sum)


