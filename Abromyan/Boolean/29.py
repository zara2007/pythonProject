x,y,x1,y1,x2,y2 = map(float,input().split())
otvet = (x>x1 and y>y1) and (x<x2 and y<y2)
print(otvet)