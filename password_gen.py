# Password Generator
# sprobowac z hashowac haslo i dowiedziec sie co to jest
# Wylosuj wyniki


import string
import random


# Inputs from user - Requiments for password

while True:
    passwordLenght = int(input('How long your password needs to be?: '))
    symbols = passwordLenght
    passReqUpper = int(
        input(f'How many Uppercase letters? (You can use {symbols} symbols): '))
    symbols = passwordLenght - passReqUpper
    passReqLower = int(
        input(f'How many Lowercase letters? (You can use {symbols} symbols): '))
    symbols = passwordLenght - passReqUpper - passReqLower
    passReqPunkt = int(
        input(f'How many Punctuation letters? (You can use {symbols} symbols): '))
    symbols = passwordLenght - passReqUpper - passReqLower - passReqPunkt
    passReqDigit = int(
        input(f'How many Digits letters? (You can use {symbols} symbols): '))
    passReqLenght = passReqUpper + passReqLower + passReqPunkt + passReqDigit
    if passReqLenght > passwordLenght:
        print('Password cannot be created as you putted to many symbols in lenght of the password')
        continue
    else:
        break

# Lists for creating and randomizing Password

password = []
ranUpper = []
ranLower = []
ranPunkt = []
ranDigit = []


for upper in range(passReqUpper):
    upper = random.choice(string.ascii_uppercase)
    ranUpper.append(upper)

for lower in range(passReqLower):
    lower = random.choice(string.ascii_lowercase)
    ranLower.append(lower)

for punkt in range(passReqPunkt):
    punkt = random.choice(string.punctuation)
    ranPunkt.append(punkt)

for digit in range(passReqDigit):
    digit = random.choice(string.digits)
    ranDigit.append(digit)


# Lenght of leftovers symbols for future randomazing

dlugoscHasla = passwordLenght - passReqLenght


# If user havent used all "Symbols", random the rest

listOfstringMethods = string.ascii_letters + string.punctuation + string.digits


for passwordRandom in range(dlugoscHasla):
    passwordRandom = random.choice(listOfstringMethods)
    password.append(passwordRandom)

# Randomize symbols, letters and digits

nowaLista = password + ranUpper + ranLower + ranPunkt + ranDigit

random.shuffle(nowaLista)

# Print password

print('Your secure password is: ', *nowaLista, sep='')
