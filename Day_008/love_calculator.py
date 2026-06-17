# # Love Calculator
def calculate_love_score(name1, name2):
    names = (name1 + name2).lower()

    true_score = (
        names.count("t") +
        names.count("r") +
        names.count("u") +
        names.count("e")
        )

    love_score = (
        names.count("l") +
        names.count("o") +
        names.count("v") +
        names.count("e")
        )

    print(f"{true_score}{love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")

# def calculate_love_score():
#     name1 = input("What is the first name?\n")
#     name2 = input("What is the second name?\n")
#     names = (name1 + name2).lower()

#     true_score = (
#         names.count("t") +
#         names.count("r") +
#         names.count("u") +
#         names.count("e")
#         )

#     love_score = (
#         names.count("l") +
#         names.count("o") +
#         names.count("v") +
#         names.count("e")
#         )

#     print(f"{true_score}{love_score}")

# calculate_love_score()
