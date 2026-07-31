import random
import art 

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Regras do Ás
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) # O Ás passa a valer 1 e não 11
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You Lose!"
    elif c_score > 21:
        return "Opponent went over. You Win!"
    elif u_score > c_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, current score: {user_score}")
        print(f"Computer's firt card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            while True:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if user_should_deal == "y":
                    user_cards.append(deal_card())
                    break
                elif user_should_deal == "n":
                    game_over = True
                    break
                else: 
                    print("Invalid option!")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if play == "y":
        print("\n" * 20)
        play_game()
    elif play == "n":
        print("Goodbye!")
        break
    else: 
        print("Invalid option!")
