class AgeTooSmallError(Exception):
    pass

while True:
    try:
        age=int(input("Enter Age:"))
        if (age<18):
            print("You Enter Age less then 18..")
            raise AgeTooSmallError("Age Less than 18")
        else:
            print("Please Enter Age less Than 18..")
    except TypeError:
        print('Please Enter Age More Than 18..')
