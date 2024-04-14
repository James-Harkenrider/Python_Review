import random
import os

def number_compare(user_guess, generated_number):
    if user_guess > generated_number:
        print("Too high!")
        return 1
    elif user_guess < generated_number:
        print("Too low!")
        return 1
    elif user_guess < 0 or user_guess > 100:
        print("Guess was out of bounds, try again.")
        return 0
    else:
        print("You guessed it!")
        return 11

play = True
while play:
    chances = 10
    difficulty = input("Pick a difficulty; selected (E) for Easy and (H) for Hard: ")
    if difficulty.lower() == 'h':
        chances = 5
    
    random_number = random.randint(0,100)
    print(f"You have {chances} chances to guess the number!")
    while chances > 0:
        guess = int(input("Pick a number between 0 and 100: "))
        chances -= number_compare(guess, random_number)
        if chances > 0:
            print(f"You have {chances} chance(s) remaining")

    if chances != 0:
        print("You win!")
    else:
        print("Sorry, better luck next time!")
        
    play_again = input("Play again? (Y) for yes, (N) for no.: ")
    if play_again.lower == 'n':
        play = False