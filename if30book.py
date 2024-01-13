a = int(input())
if a % 2 == 0 and a < 100 and a >= 10:
    print("четное двузначное число")
elif a % 2 != 0 and a > 99:
    print("нечетное трехзначное число")
elif a % 2 == 0 and a > 99:
    print("четное трехзачное число")
elif a % 2 != 0 and a < 100:
    print("нечетное двухзначное число")
else:
    print("qate")