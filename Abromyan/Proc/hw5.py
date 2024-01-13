def aANDb(a,b):
    print(a=b,b=a)
    return a,b

a,b = map(int,input().split())
print(aANDb(a,b))