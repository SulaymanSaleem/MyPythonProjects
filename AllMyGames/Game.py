import random
print("""
You have 3 tries to guess a number between and including 1-9"
Each time you run the script the number changes!
""")

secret_number = random.randint(1, 9)
tries = 0
guess_limit = 3
while tries < guess_limit:

    try:
        guess_number = int(input("Guess: "))
        if guess_number == secret_number:
            msg = f'Well done! The number was {secret_number}'
            print(msg)
        elif guess_number < 1 or guess_number > 9:
            print("Enter a number between 1 and 9")

        elif guess_number != secret_number and tries == 2:
            print("YOU LOSE!!!")
            print("The number was ", secret_number)
            break
        else:
            print("Try again...")
            tries = tries + 1

    except ValueError:
        print("Enter a number")
