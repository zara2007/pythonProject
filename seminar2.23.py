a = int(input())
if 1<=a<=5:
    print(a+10)
elif 10<=a<=20:
    print(a-5)
elif a<0 or a>1000:
    print(a*3)
else:
    print(0)