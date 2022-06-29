
masterpass = input("what is the master password?\n")
with open('masterpassword.txt','r') as m:
    a = m.readlines()
    b = ''.join(a)
if masterpass ==b:

    def add():
        name = input("Account Name ")
        pwd = input("password ")
        with open("passwords.txt","a") as f :
            f.write(f"{name} | {password}\n")

    def view():
        with open('passwords.txt','r') as f:
            for line in  f.readlines():
              print(line)


    while True:
        mode = input("would you like to add a password or view the existing ones? (type:- view, add, q to quit)\n").lower()
        if mode == "q": 
            break
        
        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid Input")
            continue
else:
    print("wrong password")