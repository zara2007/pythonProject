x,y,x1,y1 = map(int,input().split())
otvet = (y==y1 and abs(x-x1)==1) or (x==x1 and abs(y-y1)==1) or (abs(x-x1)==1  and abs(y-y1)==1)
print(otvet)

