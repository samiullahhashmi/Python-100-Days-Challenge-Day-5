import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ''

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n")) 
num_numbers = int(input(f"How many numbers would you like?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))

for char in range(1, num_letters + 1):
    password += random.choice(letters)

for char in range(1, num_numbers + 1):
    password += random.choice(numbers)

for char in range(1, num_symbols + 1):
    password += random.choice(symbols)

new_pass = str(password)

print("Your password could be : " + new_pass)