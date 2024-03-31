email = input("Enter your email: ")
password = int(input("Enter your password: "))

authorized = False

while authorized != True:
    password = int(input("Enter your password: "))
    if len(password) < 8:
        print("Please enter at least 8 characters.")
    else:
        repeat_password = int(input("Please confirm your password: "))
        if password == repeat_password:
            print("Account created")
            authorized = True
        else:
            print(int("Passwords do not match"))