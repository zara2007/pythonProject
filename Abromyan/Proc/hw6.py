def osu(a,b):
    if a>b:
        print(b,a)
    else:
        print(a,b)
    return
a,b = map(int,input().split())
print(osu(a,b))