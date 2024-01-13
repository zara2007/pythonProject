a = int(input())
otvet = (a//100<a%100//10<a%100%10) or (a//100>a%100//10>a%100%100)
print(otvet)