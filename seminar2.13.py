a,b,c = map(int,input().split())
if a>b and a>c and b<a and b<c:
    print(a-b)
elif a>b and a>c and c<a and c<b:
    print(a-c)
elif b>a and b>c and a<b and a<c:
    print(b-a)
elif b>a and b>c and c<b and c<a:
    print(b-c)
elif c>a and c>b and a<b and a<c:
    print(c-a)
else:
    print(c-b)