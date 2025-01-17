def main():
    """
    Main function to prompt the user for input, determine if the input is even or odd,
    and print the result.
    """
    # Prompt the user to input an integer
    x = int(input("What's x? "))
    
    # Check if the number is even or odd using the is_even function
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    """
    Function to check if a given number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is even, False otherwise.
    """
    # Check if the number is divisible by 2 with no remainder
    if n % 2 == 0:
        return True
    else:
        return False

# Execute the main function
main()
