def checkEmail (email):
    if "@" in email:
        print ("Email is valid.")
    else:
        print ("Invalid Email.")

email = input ("Enter email: ")
checkEmail (email)