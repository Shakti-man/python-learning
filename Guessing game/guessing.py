from logo import *
import random
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
x = random.randint(1,100)
def easy():
    live_count=10
    print(f"You have {live_count} attempts remaining to guess the number.")
    for i in range (live_count+1):
            if live_count!=0:
                guess_number=int(input("Make a guess: "))
                if guess_number>x:
                    print("Too high.\nGuess again.")
                    live_count-=1
                    print(f"You have {live_count} attempts remaining to guess the number.")
                elif guess_number<x:
                    print("Too low.\nGuess again.")
                    live_count-=1
                    print(f"You have {live_count} attempts remaining to guess the number.")
                else:
                    print(f"You guessed correct {guess_number}")
                    break
            else:
                print("You ran out of lives.\nGame over!")
def hard():
    live_count=5
    print(f"You have {live_count} attempts remaining to guess the number.")
    for i in range (live_count+1):
            if live_count!=0:
                guess_number=int(input("Make a guess: "))
                if guess_number>x:
                    print("Too high.\nGuess again.")
                    live_count-=1
                    print(f"You have {live_count} attempts remaining to guess the number.")
                elif guess_number<x:
                    print("Too low.\nGuess again.")
                    live_count-=1
                    print(f"You have {live_count} attempts remaining to guess the number.")
                else:
                    print(f"You guessed correct {guess_number}")
                    break
            else:
                print("You ran out of lives.\nGame over!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    easy()
elif difficulty=="hard":
    hard()
else:
    print("invalid difficulty level")