import random
user_input = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_input = random.randint(0,2)
print(f"Computer chose {computer_input}\n")
if (user_input == computer_input):
    print("Draw")
elif(user_input == 0 and computer_input == 1):
    print("You Lose")
elif(user_input == 0 and computer_input == 2):
    print("You Win")
elif(user_input == 1 and computer_input == 0):
    print("You Win")
elif(user_input == 1 and computer_input == 2):
    print("You Lose")
elif(user_input == 2 and computer_input == 1):
    print("You Win")
elif(user_input == 2 and computer_input == 0):
    print("You Lose")
else:
    print("Choose valid choice pls")




