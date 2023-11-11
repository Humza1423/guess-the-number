import random

print("Guess a Number between 1 and 9")
randomNumber=random.randint(1, 9)

chances=0


while chances<5:
    guess=int(input("Enter your guess: "))
    if guess==randomNumber:
        print("Congratulations! You guessed correct!")

    elif guess<randomNumber:
            print("good try, but not close enough")
    else:
            print("far, try again.")
            chances=chances+1
if not chances<5:
      print("You lost the game.", randomNumber)



    