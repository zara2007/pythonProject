x,y,x1,y1 = map(int,input().split())
otvet = ((x1+y1)%2==1 and (x+y)%2==1) or ((x1+y1)%2==0 and (x+y)%2==0)
print(otvet)