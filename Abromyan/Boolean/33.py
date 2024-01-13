a,b,c = map(int,input().split())
otvet = a<b+c or b<a+c or c<a+b
print(otvet)