a,b,c = map(int,input().split())
otvet = a**2==(b**2)+(c**2) or b**2==(c**2)+(a**2) or c**2==(a**2)+(b**2)
print(otvet)