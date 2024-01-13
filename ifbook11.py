a,b = map(int,input().split())
if a!=b:
    if a>b:
        print(a,a)
    else:
        print(b,b)
else:
    print(a,b)