def main():
    # Ask the user for their name, remove leading and trailing whitespace, and capitalize the name
    name = input("What is your name? ").strip().title()

    # Call the hello function to greet the user
    hello(name)

def hello(to="world"):
    # Print a greeting message to the user
    print("hello,", to)

# Execute the main function
main()
