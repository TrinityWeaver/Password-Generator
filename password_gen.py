# Password Generator
# sprobowac z hashowac haslo i dowiedziec sie co to jest
# Wylosuj wyniki


import string
import random
import bcrypt
import csv
import os


# Function for attaching symbols left into string
def symbolsFun(firstValue, secondValue=0, thirdValue=0, fourthValue=0):
    symbolsFun = firstValue - secondValue - thirdValue - fourthValue
    return symbolsFun


# Function for calculation how much more symbols program can put inside teh password
def passReqLenghtFunction(fv, fv2, fv3, fv4):
    suma = fv + fv2 + fv3 + fv4
    return suma

# Function for randomizing chosen numbers of symbols


def randomSym(sym):
    if sym == 'passReqUpper':
        for upper in range(passReqUpper):
            upper = random.choice(string.ascii_uppercase)
            ranUpper.append(upper)
    elif sym == 'passReqLower':
        for lower in range(passReqLower):
            lower = random.choice(string.ascii_lowercase)
            ranLower.append(lower)
    elif sym == 'passReqPunkt':
        for punkt in range(passReqPunkt):
            punkt = random.choice(string.punctuation)
            ranPunkt.append(punkt)
    elif sym == 'passReqDigit':
        for digit in range(passReqDigit):
            digit = random.choice(string.digits)
            ranDigit.append(digit)


print('Password Generator v.2.0\nAuthor: Sebastian Marynicz')

firstChoice = input(
    'Would you like to create randomized password or hashed?\n Type in "Random" or "Hash": ')
url = input('Please provide an url for password: ')
userName = input('Please provide a username/email: ')

loopsforpass = False


while firstChoice == "Random":
    print('Default password created by Generator will be 10 symbols lenght,\nwith 2 uppercase,\nwith 2 lowercase,\nwith 2 symbols\nwith 2 digits.')
    defaultPassword = input(
        'Would you like to proceed with default or customized option?\nType in "Default" or "Custom": ')
    if defaultPassword == 'Custom':
        passwordLenght = int(input('How long your password needs to be?: '))
        symbols = symbolsFun(passwordLenght)
        passReqUpper = int(
            input(f'How many Uppercase letters? (You can use {symbols} symbols): '))
        symbols = symbolsFun(passwordLenght, passReqUpper)
        passReqLower = int(
            input(f'How many Lowercase letters? (You can use {symbols} symbols): '))
        symbols = symbolsFun(passwordLenght, passReqUpper, passReqLower)
        passReqPunkt = int(
            input(f'How many Punctuation letters? (You can use {symbols} symbols): '))
        symbols = symbolsFun(passwordLenght, passReqUpper,
                             passReqLower, passReqPunkt)
        passReqDigit = int(
            input(f'How many Digits letters? (You can use {symbols} symbols): '))
        passReqLenght = passReqLenghtFunction(
            passReqUpper, passReqLower, passReqPunkt, passReqDigit)
        if passReqLenght > passwordLenght:
            print(
                'Password cannot be created as you put to many symbols in lenght of the password')
            continue
        else:
            loopsforpass = True
            break

    else:
        loopsforpass = True
        passReqUpper = 2
        passReqLower = 2
        passReqPunkt = 2
        passReqDigit = 2
        passwordLenght = 10
        passReqLenght = 8
        break

# Lists for creating and randomizing Password
# Lenght of leftovers symbols for future randomazing
# If user havent used all "Symbols", random the rest
# Randomize symbols, letters and digit
# Print password
password = []
ranUpper = []
ranLower = []
ranPunkt = []
ranDigit = []
if loopsforpass:
    randomSym('passReqUpper')
    randomSym('passReqLower')
    randomSym('passReqPunkt')
    randomSym('passReqDigit')

    theLenghtofPassword = passwordLenght - passReqLenght
    listOfstringMethods = string.ascii_letters + string.punctuation + string.digits

    for passwordRandom in range(theLenghtofPassword):
        passwordRandom = random.choice(listOfstringMethods)
        password.append(passwordRandom)

    newPassword = password + ranUpper + ranLower + ranPunkt + ranDigit
    random.shuffle(newPassword)

    print('Your secure password is: ', *newPassword, sep='')

    randomPassword = ''.join(newPassword)
    if os.path.exists('./secrets.csv') == True:
        with open('secrets.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([f'{url}', f'{userName}', f'{randomPassword}'])

    else:
        with open('secrets.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["url", "Username", "Password"])
            writer.writerow(
                [f'{url}', f'{userName}', f'{randomPassword}'])

        # Hashing Password
if loopsforpass == False:
    while firstChoice == 'Hash':
        passwordToHash = input('Provide a password for hashing: ')
        passBytes = bytes(f'{passwordToHash}', 'utf-8')
        hashedPass = bcrypt.hashpw(passBytes, bcrypt.gensalt(15))
        if bcrypt.checkpw(passBytes, hashedPass):
            print('Password macthes!')
            hashedPass = hashedPass.decode('utf-8')
            if os.path.exists('./secrets.csv') == True:
                with open('secrets.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow([f'{url}', f'{userName}', f'{hashedPass}'])
                break
            else:
                with open('secrets.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow(["url", "Username", "Password"])
                    writer.writerow(
                        [f'{url}', f'{userName}', f'{hashedPass}'])
                break
        else:
            print('Password dont match!')
            continue
    else:
        print('You left program!')
