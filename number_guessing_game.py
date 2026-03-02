# Number guessing game
import random
import time
no_of_tries = 5
orig_number = random.randint(1, 10)
while no_of_tries:
    guess_number = int(input("Enter a number: "))
    time.sleep(3)
    if orig_number == guess_number:
        print(f"You have guessed the correct number: {guess_number} \U0001F600")
        break
    else:
        no_of_tries -= 1
        if no_of_tries != 0:
            print(f"You guessed a wrong number\nTry Again\nLeft turns are: {no_of_tries}")
        else:
            print(f"You loose the game\n Original number is {orig_number}")
    print('-----------------------------------------------')