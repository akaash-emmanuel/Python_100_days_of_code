# BlackJack project
# rules : 1. goal is to not go over 21
#         2. if the cards in hand is over 21, its a bust and we lose immediately
#         3. cards from 2->10 count as their facevalue
#         4. jack and king and queen count as 10
#         5. ace can count as 1 or 11, this depends on you, on how far you are from the goal value of 21
#         6. if the score of you and the dealer is a draw
#         7. if the dealer has a count of <17 i.e 16 or under, then they must take another card

import random
import math
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return score

def print_result(user_score, computer_score):
    if user_score > 21:
        print("You Lose")
    elif computer_score > 21:
        print("You Win")
    elif user_score == computer_score:
        print("It's a draw")
    elif user_score > computer_score:
        print("You Win")
    else:
        print("You Lose")

def blackjack():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards : {user_cards}, current score : {user_score}")
    print(f"Computer's first card : [{computer_cards[0]}]")


    while user_score < 21:
        yorno = input("Type 'y' to get another card or type 'n' to pass: ")
        if yorno == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards : {user_cards}, current score : {user_score}")
        else:
            break
    
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, final score : {computer_score}")

    print_result(user_score, computer_score)

blackjack()








