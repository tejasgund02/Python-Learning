password = "12345678"

if len(password) < 8:
    print("Password is too short")
elif len(password) < 16:
    print("Password is ok")
else:
    print("Password is too long")
