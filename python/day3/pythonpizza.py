print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25
if pepperoni == "Y":
    bill += 30
if pepperoni == "N":
    bill += 40
if extra_cheese == "Y":
    bill += 50
if extra_cheese == "N":
    bill += 60

print(f"Your final bill is ${bill}")