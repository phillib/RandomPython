# Uses list comprehension to create a list of squares in the range 
# of 1 to 11 that are divisible by 2.

even_squares = [x**2 for x in range(1, 12) if (x**2) % 2 == 0]

print even_squares
