login , password = map(str,input().split())
if login == "user" and password == "qwerty":
    print("Authentication comleted")
else:
    print("Invalid login or password")