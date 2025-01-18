# Prompt the user to input their name
name = input("What's your name? ")

# Match the input name to predefined cases
match name:
    case "Harry":
        # If the name is "Harry", print Gryffindor
        print("Gryffindor")
    case "Hermione":
        # If the name is "Hermione", print Gryffindor
        print("Gryffindor")
    case "Ron":
        # If the name is "Ron", print Gryffindor
        print("Gryffindor")
    case "Draco":
        # If the name is "Draco", print Slytherin
        print("Slytherin")
    case _:
        # For any other name, print Who?
        print("Who?")
