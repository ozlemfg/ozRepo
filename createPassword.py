#       Create a password, validate it, ask again until it is valid, print the message
#       Password rule: at least 6 characters, contains at least one number

print("Password rule: 6 characters, contains at least one number")


while True:
    pwd = input(f"Create password:")

    if len(pwd) < 6:
        print("password must be at least 6 char")
        continue
    if not any(char.isdigit() for char in pwd):
        print("Pwd must contain at least 1 digit")
        continue
    break
print(f"your pwd is {pwd}")



