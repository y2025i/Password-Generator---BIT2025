def password_strength(password):
    space = False
    for char in password:
        if char==' ':
            space = True
            break
    if space==True:
        print("You cant have space in password!")
        return False
    if len(password) < 6:
        print("Password is too short!")
        return False
    counter = 0
    for char in password:
        if char.isdigit():
            counter += 1
            break
    for char in password:
        if char.isalpha():
            counter += 1
            break
    for char in password:
        if (char>='!' and char<='/') or (char>=':' and char<='@') or (char>='[' and char<=chr(96) or (char>='{' and char<=chr(126))):
            counter += 1
            break
    if counter==3:
        print("Password is strong!")
        return True
    elif counter==2:
        print("Passoword is medium")
        return True
    elif counter==1:
        print("Password is weak!")
        return True


password = input("Enter your password: ")
while password_strength(password)==False:
    password = input("Enter your password: ")