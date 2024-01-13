n=int(input("Insert amount in KZT:\n"))
print("[1] USD")
print( "[2] EUR")
print("[2] RUB")
m=int(input("Choose currency:\n"))
#USD=420;EUR=510;RUB=5.8
if m==1:
    print(float(n/420 ), "USD")
elif m==2:
    print(float(n/510) , "EUR ")
else:
    print(float(n/5.8 ), "RUB")
