import random

DECK = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10},
]

def deal_card():
    return random.choice(DECK).copy()

def calculate_score(cards):

    values = [card["value"] for card in cards]

    if sum(values) == 21 and len(cards) == 2:
        return 0

    while 11 in values and sum(values) > 21:

        ace = next(card for card in cards if card["value"] == 11)
        ace["value"] = 1

        values = [card["value"] for card in cards]

    return sum(values)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "🤝 Draw!"

    if computer_score == 0:
        return "💀 Lose! Dealer has Blackjack."

    if user_score == 0:
        return "🎉 Blackjack! You Win!"

    if user_score > 21:
        return "💥 You went over. You Lose."

    if computer_score > 21:
        return "🎉 Dealer went over. You Win!"

    if user_score > computer_score:
        return "🏆 You Win!"

    return "❌ You Lose."

def dealer_turn(cards):
    score = calculate_score(cards)

    while score != 0 and score < 17:
        cards.append(deal_card())
        score = calculate_score(cards)

    return cards

def start_game():
    return{
        "user_cards": [deal_card(), deal_card()],
        "computer_cards": [deal_card(), deal_card()],
        "game_over": False,
        "message": "",
    }
