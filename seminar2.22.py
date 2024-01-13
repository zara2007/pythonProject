print("ENTER COORDINATES OF LADYA")
xl, yl = map(int, input().split())
print("ENTER COORDINATES OF FIGURE")
xf, yf = map(int, input().split())

if xl == xf or yl == yf:
    print("YES")
else:
    print("NO")