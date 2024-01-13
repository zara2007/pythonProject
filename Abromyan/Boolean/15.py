a,b,c = map(int,input().split())
otvet = (a%2==0 and b%2==0 and c%2==1) or (a%2==1 and b%2==0 and c%2==0) or (a%2==0 and b%2==1 and c%2==0)
print(otvet)
