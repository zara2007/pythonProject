a, b = map(int, input().split())
otvet = (a%2!=0 and b%2==0) or (b%2!=0 and a%2==0)
print(otvet)

