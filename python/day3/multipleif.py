print("Welcome to the multiple if statement example!")
height = int(input("Please enter your height in centimeters: "))
bill = 0:

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age: "))
    if age <= 12:
        bill = 5
        print("You are a child, please pay $5")
    elif age <= 18:
        bill = 7
        print("You are a teenager, please pay $7")
    else:
        bill = 12
        print("You are an adult, please pay $12")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")