import string as st
import random as rd

def randomEmailGenerator(name):

    email = ""
    email = name[1]+"."+name[0]+"".join(rd.choices(st.digits,k=3))+"".join(rd.choices(st.ascii_lowercase,k=3))+"@gmail.com"
    return email

try:
    print("\nEnter 0 if you want to stop ")
    while True:

        name = input("\nEnter your Fiest name and Last name : ").split(" ")
        if name != "0":
            email = randomEmailGenerator(name)
            print("\nYour email is : ",email)
        else:
            break
except:
    pass