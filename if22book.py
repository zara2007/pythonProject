a,b = map(int,input().split())
if a>0 and b>0:
    print(1)
elif a>0 and b<0:
    print(4)
elif a<0 and b<0:
    print(3)
else:
    print(2)
