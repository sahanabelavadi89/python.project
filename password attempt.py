user_name='sahana'
user_password=248
name=input('enter your name:')
if name==user_name:
    for i in range(1,4):
        password=int(input('enter your password:'))
        if password==user_password:
            print('Welcome')
        else:
            print(i,"attempt is done")
            print(3-i,"attempt is remaining")
else:
    print("enter valid name")

