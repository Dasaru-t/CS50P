# Prompt the user to input an integer value for x
x = int(input("What's x? "))

# Check if x is even or odd using the modulus operator
if x % 2 == 0:
    # If the remainder of x divided by 2 is 0, x is even
    print("Even")
else:
    # If the remainder of x divided by 2 is not 0, x is odd
    print("Odd")
