import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if difficulty == 'easy':
    attempts = attempts + 10
else: 
    attempts = attempts + 5

number = random.randint(1, 100)

def comparison(guessed_num):
    if guessed_num > number:
        print("Too high")
    elif guessed_num < number:
        print("Too low")
    else:
        print(f"Yes!, I thought of {guessed_num} and you guessed it right!")
        return True
    return False

while attempts > 0:
    guess = int(input("Make a guess: "))
    if comparison(guess):
        break
    attempts = attempts - 1
    print(f"You have {attempts} attempts remaining")

if attempts == 0:
    print(f"You ran out of attempts! the number was {number}")

    

