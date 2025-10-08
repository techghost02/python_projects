###  NUMBER GUESSING PROJECT  ###
# The computer picks a number randomly and the user has to guess it

# Import necessary libraries
import random

def play_game():    
    # Introduction
    print("Welcome to the NUMBER GUESSING GAME!!")
    print("Game rules : \n \
        1. Aim is to have lowest total score. \n \
        2. +1 for every try if guess is without a clue. \n \
        3. +2 for every try if guess is with clue. \n")

    print("Let the games begin!")

    gameplay = True
    points = 0
    games_Played = 0

    while gameplay == True:
        # Define the game boundaries
        while True:
            try:
                low_Range = int(input("Enter the low range : "))
                high_Range = int(input("Enter the high range : "))
                if low_Range >= high_Range:
                    print("Low range must be less than high range.")
                    continue
                break
            except ValueError:
                print("Invalid input!")
        comp_Number = random.randint(low_Range, high_Range)

        # Initialise variables to track user response
        corret_Ans = False
        tries = 0
        previous_guesses = set()

        # Prompt the user until the correct number is guessed
        while not corret_Ans:
            while True:
                try:
                    user_Number = int(input("\nGuess a number: "))
                    if low_Range < user_Number < high_Range:
                        break
                    else:
                        print(f"Enter a valid number inside the range ({low_Range}-{high_Range})")
                except ValueError:
                    print("Invalid input! Please enter an integer.")

            points +=1
            tries +=1

            # Check if the user is not typing the same guess again
            if user_Number in previous_guesses:
                print("Bzzzzzz! Bzzzzzz! You typed this number last time!")
            else:
                previous_guesses.add(user_Number)

            # Check if the guess is correct
            if user_Number == comp_Number:
                corret_Ans = True
            else:
                print("❌ Nah! Try again!")
                # Ask if the user wants a clue
                while True:
                    clue_Needed = input("Would you like a clue? \n\"Y\" for yes \"N\" for no : ").upper()
                    if clue_Needed == "Y" or clue_Needed == "N":
                        break
                    else:
                        print(f"Enter a valid response. \"Y\" for yes \"N\" for no.")

                # Provide appropriate clue
                if clue_Needed == "Y":
                    points += 1
                    if user_Number > comp_Number:
                        print("My number is smaller than your guess!")
                    else:
                        print("My number is greater than your guess!")
                else:
                    print("Okay okay! Carry on! Best of Luck!")

        print(f"\n🎉 Congratulations!! You guessed the number in {tries} tries and your current points are {points} points.")
        games_Played += 1

        # Check if a new round is to be played
        while True:
            user_cont = input("\nWould you like to play more? ").upper()
            if user_cont == "Y" or user_cont == "N":
                break
            else:
                print(f"Enter a valid response. \"Y\" for yes \"N\" for no.")

        if user_cont == "N":
            gameplay = False
        else:
            print("Yay! Let\'s play the next round!\n")

    # End credits
    print("\nYou have decided to quit the game.\nGAME STATS :")
    print(f"1. Games played : {games_Played}")
    print(f"2. Total points scored : {points}")
    print("Goodbye!")

if __name__ == "__main__":
    play_game()
