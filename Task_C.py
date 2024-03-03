print("Welcome to user name checking system!")
user_name=str(input("Enter the User Name:- "))
k=0
i=0
if(len(user_name)<5):
    print("Try Again\nUser Name is invalid")
else:
    k=1
for ch in user_name:
    if(ch.isalnum()):
        i=i+1
    else:
        i=-1
        print("Try Again\nUser Name is invalid")
        break
if(k==1 and i>=0):
    print("User Name is valid")