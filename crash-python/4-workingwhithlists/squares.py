squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    # more ease
    #squares.append(value ** 2)

print(squares)

# Other way
squaress = [value ** 2 for value in range(1, 11)]
print(squaress)

print(squaress[:2])
print(squaress[2:])
