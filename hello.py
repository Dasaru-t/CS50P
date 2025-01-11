def main():
    """
    Main function to handle user input and initiate the greeting process.
    Prompts the user for their name, formats it, and passes it to the hello function.
    """
    # Ask the user for their name, remove leading and trailing whitespace, and capitalize the name
    name = input("What is your name? ").strip().title()

    # Call the hello function to greet the user with the formatted name
    hello(name)

def hello(to="world"):
    """
    Function to print a greeting message.
    Accepts a name as an argument (default is "world") and prints a personalized greeting.
    """
    # Print a greeting message to the user
    print("hello,", to)

# Execute the main function
main()
