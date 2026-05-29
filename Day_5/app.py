import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', 'A', 
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '=', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password? \n"))
n_symmbols = int(input("How many symbols would you like? \n"))
n_numbers = int(input("How many numbers would you like? \n"))

# Easy Level
# password = ""
# for char in range(0, n_letters):
#         password += random.choice(letters)

# for char in range(0, n_symmbols):
#         password += random.choice(symbols)

# for char in range(0, n_numbers):
#         password += random.choice(numbers)

# print(f"Your password is : \n{password}")

# Hard Level
password_list = []
for char in range(0, n_letters):
        password_list.append(random.choice(letters))

for char in range(0, n_symmbols):
        password_list.append(random.choice(symbols))

for char in range(0, n_numbers):
        password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
        password += char

print(f"Your password is : \n{password}")
