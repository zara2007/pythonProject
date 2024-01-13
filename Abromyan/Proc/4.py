def TrianglePS(a):
    P = 3*a
    S = a**2 * (3**0.5/4)
    return P , S

a = int(input())
print(TrianglePS(a))

