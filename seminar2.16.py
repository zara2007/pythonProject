a,b,c = map(int,input().split())
if a>10 and b>10 and c>10 and a%5==0 and b%5==0 and c%5==0:
    print("YES")
else:
    print("NO")
