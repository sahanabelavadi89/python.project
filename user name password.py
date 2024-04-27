username=["Sahana","Anusha"]
password=['123','234']
name=input("enter your name")
for a,b in enumerate(username):
    if b==name:
        password1=input("enter your password")
        if password1==password[a]:
            print('welcome')