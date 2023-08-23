import re

def validate_email(email):
    pattern= r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+'
    return bool(re.fullmatch(pattern,email))

def add_email():
    ip_email=input("Enter an email address:")
    if validate_email(ip_email):
        with open("add_emails.txt","a") as file:
            file.write(ip_email + "\n")
            print("The email you entered is valid, This goes into file")
    else:
        print("The email you entered is not valid, Do you want to take chances if yes press ENTER")

    choose = input("Do you want validate emails ?(yes or no): ")
    if choose.lower()== 'yes':
        add_email()
    else:
        print("OK, Thank You")
add_email()
