# Prompt the user to input a score as an integer
score = int(input("Score: "))

# Determine the letter grade based on the score range
if score <= 100 and score >= 90:
    # If the score is between 90 and 100 (inclusive), assign grade "A"
    print("A")
elif score < 90 and score >= 80:
    # If the score is between 80 and 89 (inclusive), assign grade "B"
    print("B")
elif score < 80 and score >= 70:
    # If the score is between 70 and 79 (inclusive), assign grade "C"
    print("C")
elif score < 70 and score >= 60:
    # If the score is between 60 and 69 (inclusive), assign grade "D"
    print("D")
else:
    # If the score is below 60, assign grade "F"
    print("F")
