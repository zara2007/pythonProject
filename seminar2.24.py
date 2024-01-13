a,b,c,d = map(int,input().split())
if a>5 and b>5 and c>5 and d>5 and b%4==0 and d%3!=0:
    print("YES")
else:
    print("NO")
