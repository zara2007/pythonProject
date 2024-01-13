a,b,c = map(int,input().split())
if a>b and a>c and b<c :
    print(a ,b)
elif a>b and a>c and c<b:
    print(a,c)
elif b>a and b>c and a<c:
    print(b ,a)
elif b>a and b>c and c<a:
    print(b,c)
elif c>a and c>b and a<b:
    print(c ,a)
else:
    print(c,b)
