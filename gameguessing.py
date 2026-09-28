import random

def play():
    low, high, max_attempts = 1, 100, 7
    secret_number = random.randint(low, high)
    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts.\n")
    
    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"guess #{attempt}: "))
                break
            except ValueError:
                print("Please enter a whole number.")
        if  guess > secret_number:
            print("Too high!\n")
        else:
            print(f"correct! you got it in {attempt} attempts.")
            return
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
if __name__ == "__main__":
    while True:
        play()
        if input("\nplay again? (y/n): ").strip().lower() != 'y':
            print("Thanks for playing!")
            break