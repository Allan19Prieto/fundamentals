
for digic in range(1, 101):
    if digic % 3 == 0 and digic % 5 == 0:
        print("FizzBuzz")
    elif digic % 3 == 0:
        print("Fizz")
    elif digic % 5 == 0:
        print("Buzz")
    else:
        print(digic)


