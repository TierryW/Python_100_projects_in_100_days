def make_card(rank):
    rank = str(rank)

    left = rank.ljust(2)
    right = rank.rjust(2)

    return f"""
+---------+
|{left}       |
|         |
|         |
|         |
|       {right}|
+---------+
""".strip("\n")


ACE = make_card("A")
TWO = make_card("2")
THREE = make_card("3")
FOUR = make_card("4")
FIVE = make_card("5")
SIX = make_card("6")
SEVEN = make_card("7")
EIGHT = make_card("8")
NINE = make_card("9")
TEN = make_card("10")
JACK = make_card("J")
QUEEN = make_card("Q")
KING = make_card("K")

BLANKCARD = """
+---------+
|XXXXXXXXX|
|XXXXXXXXX|
|XXXXXXXXX|
|XXXXXXXXX|
|XXXXXXXXX|
+---------+
""".strip("\n")

CARD_ART = {
    "A": ACE,
    "2": TWO,
    "3": THREE,
    "4": FOUR,
    "5": FIVE,
    "6": SIX,
    "7": SEVEN,
    "8": EIGHT,
    "9": NINE,
    "10": TEN,
    "J": JACK,
    "Q": QUEEN,
    "K": KING,
}
