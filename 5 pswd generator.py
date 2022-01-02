#Password Generator Project
import pyperclip
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random.shuffle(letters)
pswdletters = []
for x in range(0,int(nr_letters)):
  pswdletters.append(letters[x])

random.shuffle(numbers)
pswdnumbers = []
for x in range(0,int(nr_numbers)):
  pswdnumbers.append(numbers[x])

random.shuffle(symbols)
pswdsymbols = []
for x in range(0,int(nr_symbols)):
  pswdsymbols.append(symbols[x])

final = pswdletters + pswdnumbers + pswdsymbols
random.shuffle(final)

final = ''.join(final)

print(f'Password generated and copied to clipboard: {final}')
pyperclip.copy(final)