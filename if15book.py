a,b,c = map(int,input().split())
if a>b and c>b:
    print(a+c)
elif a>c and b>c:
    print(a+b)
elif c>a and b>a:
    print(c+b)