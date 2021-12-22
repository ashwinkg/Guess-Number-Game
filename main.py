from art import logo
import random

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =5


print(logo)
def generate_number():
    return random.randint(1,100)

def validate_the_guess(user_guessed_number,number_to_be_guessed,attempts):
    if user_guessed_number==number_to_be_guessed:
         print(f"You got it! The answer was {number_to_be_guessed}")
         return attempts
    elif user_guessed_number < number_to_be_guessed:
        print("Too low")
        return attempts-1
    else:
        print("Too high")
        return attempts-1


def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level =='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
    

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
attempts = set_difficulty()
number_to_be_guessed =  generate_number()
user_guessed_number=-1
while user_guessed_number != number_to_be_guessed:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guessed_number=int(input("Make a guess: "))
    attempts=validate_the_guess(user_guessed_number,number_to_be_guessed,attempts)
    if attempts ==0:
        print("You run out of guesses. You lose")
        break

    
    
    
    
    




