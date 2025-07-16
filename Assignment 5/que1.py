correct_userid = "admin"
correct_password = "1234"

attempts = 3

for i in range(attempts):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password.")
        if i < attempts - 1:
            print(f"You have {attempts - i - 1} attempt(s) left.\n")
        else:
            print("Too many failed attempts. Program terminated.")
