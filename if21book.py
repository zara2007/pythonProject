a,b = map(int,input().split())
if a==0 and b==0:
    print(0)
elif a!=0 and b==0:
    print(1)
elif a==0 and b!=0:
    print(2)
else:
    print(3)