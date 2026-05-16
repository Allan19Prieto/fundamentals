
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))

# in pyrhon you can concatenate string with string but not with other data types
print("Hello" + " World")  # This works

# print("Hello" + 123)  # This will raise a TypeError

# but you can convert the integer to a string before concatenating
print("Hello" + str(123)) # This works

# and converting a string to an integer will raise an error if the string is not a valid number
# print(int("Hello"))  # This will raise a ValueError
# but this will work
print(int("123")) # This works


