def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)
    if(length<6):
        print("Password must be at least 6 characters long!")
    else:
        for i in range(length):
            if(password[i].isupper()):
                upperChars+=1
            elif(password[i].islower()):
                lowerChars+=1
            elif(password[i].isdigit()):
                digits+=1
            else:
                specialChars+=1
    pass

    print("Upper:", upperChars)
    print("Lower:", lowerChars)
    print("Digits:", digits)
    print("Special:", specialChars)

    pass

password = input("Please enter password: ")
checkPassword(password)