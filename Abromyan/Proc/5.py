def rectPS (x1,y1,x2,y2):
    a = x2 - x1
    b = y2 - y1
    P = (a+b)*2
    S = a * b
    return P,S

x1,y1,x2,y2 = map(int,input().split())
print(rectPS(x1,y1,x2,y2))
