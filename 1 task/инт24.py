k = int(input()) #1-365
if k%1==0 and k%2!=0 and k%3!=0 and k%4!=0 and k%5!=0 and k%6!=0 and k%7!=0:
    print("Понедельник")
if k%2==0 and k%1!=0 and k%3!=0 and k%4!=0 and k%5!=0 and k%6!=0 and k%7!=0 :
    print("Вторник")
if k%3==0 and k%2!=0 and k%1!=0 and k%4!=0 and k%5!=0 and k%6!=0 and k%7!=0 :
    print("Среда")
if k%4==0 and k%2!=0 and k%3!=0 and k%1!=0 and k%5!=0 and k%6!=0 and k%7!=0 :
    print("Четверг")
if k%5==0 and k%2!=0 and k%3!=0 and k%4!=0 and k%1!=0 and k%6!=0 and k%7!=0:
    print("Пятница")
if k%6==0 and k%2!=0 and k%3!=0 and k%4!=0 and k%5!=0 and k%1!=0 and k%7!=0 :
    print("Суббота")
if k%7==0 and k%2!=0 and k%3!=0 and k%4!=0 and k%5!=0 and k%6!=0 and k%1!=0 :
    print("Воскресенье")
