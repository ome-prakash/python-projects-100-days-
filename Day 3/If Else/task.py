print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height>120:
    print("you can ride the rollercoaster")
    age = int(input("how old are you?"))
    if age<=12:
        bill =5
        print("child tickets are  5$")
    elif age<=18:
        bill=7
        print("youth tickets are 7$")
    else:
        bill =12
        print("adult tickets are 12$")
    want_photos= input("do u want a photo y or n")
    if want_photos == "y":
        bill +=3
        print(f"final bill {bill}")
    else:
        print(f"final bill {bill}")


else:
    print("you are not allowed")


