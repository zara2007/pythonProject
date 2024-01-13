a1,a2,b1,b2,c1,c2 = map(int,(input().split()))
print("D=",(a1*b2)-(a2*b1))
print("x=",((c1*b2)-(c2*b1))/((a1*b2)-(a2*b1)))
print("y=",((a1*c2)-(a2*c1))/((a1*b2)-(a2*b1)))

