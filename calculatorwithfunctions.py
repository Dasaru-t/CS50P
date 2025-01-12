def main():
    """
    Main function to handle user input and display the result.
    Prompts the user to input a number, calculates its square using the square function,
    and prints the result.
    """
    # Prompt the user for a number and convert the input to an integer
    x = int(input("What's x? "))

    # Calculate the square of the input and display the result
    print("x squared is", square(x))

def square(n):
    """
    Function to calculate the square of a number.
    Takes an integer n as input and returns n multiplied by itself.
    """
    return n * n

# Execute the main function
main()
