# Wallace Tyner
# Date: 05/22/2026
# PA - Decisions, Loops, Processing, Output Formatting
# This program lets the user guess a number and uses
# decisions and loops to display different outputs.

# Ask the user for information
studentName = input("Enter your name: ")
studentId = input("Enter your student ID: ")

# Display greeting
print("\n--------------------------------")
print("Welcome to the Guessing Program")
print("--------------------------------")
print(f"Student Name: {studentName}")
print(f"Student ID: {studentId}")

# Predetermined correct number
correctNumber = 5

# Track attempts
attemptCount = 0

# Ask the user for a guess
userGuess = int(input("\nGuess a number between 1 and 10: "))
attemptCount += 1

# Determine if the guess is too high, too low, or correct
if userGuess > correctNumber:
    print("Your guess is too high.")

elif userGuess < correctNumber:
    print("Your guess is too low.")

else:
    print("You guessed correctly!")

# Keep asking until the user gets it correct
while userGuess != correctNumber:

    userGuess = int(input("Try again: "))
    attemptCount += 1

    if userGuess > correctNumber:
        print("Your guess is too high.")

    elif userGuess < correctNumber:
        print("Your guess is too low.")

    else:
        print("You guessed correctly!")

# Display number of attempts
print(f"\nIt took you {attemptCount} tries to guess correctly.")

# While loop example
print("\nWhile Loop Output:")

counter = 0

while counter < 5:
    print(f"{counter + 1} incremented by 1 is {correctNumber + counter + 1}")
    counter += 1

# For loop example
print("\nFor Loop Output:")

for number in range(5):
    print(f"{number + 1} incremented by 1 is {correctNumber + number + 1}")
