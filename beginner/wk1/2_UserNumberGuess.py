import random

def play_game():
    # Introduction
    print("Welcome to the NUMBER GUESSING GAME!!")
    print("Game rules : \n \
        1. Aim is to have the lowest total score. \n \
        2. +1 for every try. \n")

    print("Let the games begin!")

    gameplay = True
    games_Played = 0
    tries = 0

    while gameplay:
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
                print("Invalid input! Please enter numbers only.")

        print(f"\nMentally select a number between {low_Range} and {high_Range}.\n")

        correct_Ans = False

        # Prompt the user until the correct number is guessed
        while not correct_Ans:
            if low_Range > high_Range:
                print("⚠️ Cheating detection: Your clues have created an impossible range!")
                print("Please play fairly next time!")
                correct_Ans = True
                break

            comp_Number = (low_Range + high_Range) // 2
            tries += 1

            user_check = input(f"My guess is number {comp_Number}. Am I correct (Y/N)? ").strip().upper()

            if user_check == "N":
                print("Okay! I will try again!")
                clue = input(f"Can I get a clue? Is your choice greater than {comp_Number}? (Y/N): ").strip().upper()

                if clue not in ["Y", "N"]:
                    print("Invalid input! Please respond with 'Y' or 'N'.")
                    tries -= 1  # Don't count invalid input
                    continue

                # Adjust range based on clue
                if clue == "Y":
                    low_Range = comp_Number + 1
                else:
                    high_Range = comp_Number - 1

                # Cheat Check: impossible range
                if low_Range > high_Range:
                    print("\n⚠️ Cheating detection: Your clues are inconsistent!")
                    print(f"(Your number cannot be both greater than {high_Range} and less than {low_Range}.)")
                    correct_Ans = True
                    break

            elif user_check == "Y":
                correct_Ans = True
            else:
                print("Invalid input! Please respond with 'Y' or 'N'.")
                tries -= 1  # Don’t count invalid tries

        if low_Range <= high_Range:
            print(f"\n🎉 Congratulations!! I guessed your number in {tries} tries.")
        else:
            print("\n❌ The game ended early due to inconsistent clues.")

        games_Played += 1

        # Check if a new round is to be played
        while True:
            user_cont = input("\nWould you like to play more? (Y/N): ").strip().upper()
            if user_cont in ["Y", "N"]:
                break
            else:
                print("Enter a valid response. 'Y' for yes or 'N' for no.")

        if user_cont == "N":
            gameplay = False
        else:
            print("\nYay! Let's play the next round!\n")

    # End credits
    print("\nYou have decided to quit the game.\nGAME STATS:")
    print(f"1. Games played: {games_Played}")
    print(f"2. Total tries: {tries}")
    print("Goodbye!")

if __name__ == "__main__":
    play_game()
