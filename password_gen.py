# Password Generator
# Requiments for password ( For now at least one capital , one symbol and one number)
# sprobowac z hashowac haslo i dowiedziec sie co to jest
# Wylosuj wyniki


import string
import random


passwordLenght = int(input('How long your password needs to be?: '))
passReqUpper = int(input('How many Uppercase letters? '))
passReqLower = int(input('How many Lowercase letters? '))
passReqPunkt = int(input('How many Punctuation letters? '))
passReqDigit = int(input('How many Digits letters? '))


# password = random.choice(string.ascii_letters)
# print(password)

password = []
ranUpper = []

listOfstringMethods = string.ascii_letters + string.punctuation + string.digits

# Upper case requiment
for upper in range(passReqUpper):
    stringUpper = random.choice(string.ascii_uppercase)
    ranUpper.append(stringUpper)

# Dlugosc hasla
dlugoscHasla = passwordLenght - passReqUpper
print(dlugoscHasla)

# Reszta co zostala random
for passwordRandom in range(dlugoscHasla):
    passwordRandom = random.choice(listOfstringMethods)
    password.append(passwordRandom)

nowaLista = password + ranUpper
print(nowaLista)
random.shuffle(nowaLista)
print(*password, *ranUpper, sep='')
print(ranUpper)
print(*nowaLista, sep='')


# Wyciagniete z for in
#    listOfStrings = [stringUpper, stringPunctuation, stringLower, stringDigit]
#    stringUpper = random.choice(string.ascii_lowercase)
#    stringPunctuation = random.choice(string.punctuation)
#    stringLower = random.choice(string.ascii_uppercase)
#    stringDigit = random.choice(string.digits)
