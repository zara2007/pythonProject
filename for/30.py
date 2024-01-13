k,n,w = map(int,input().split())
for i in range (1,k+1):
    for j in range (0,110):
        for m in range (w,1001):
            if m-(i*j)>0:
                break
print(m-(i*j))
