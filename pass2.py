import string
import random
import os
from colorama import Fore, Style

os.system('cls' or 'clear')
print(Style.RESET_ALL)

print(Fore.YELLOW + "GENERATE PASSWORD \n")

alphabet = list(string.ascii_letters)
digit = list(string.digits)
special = list("!@#$%^&*()_-")
character = list(string.ascii_letters + string.digits + "!@#$%^&*()_-")

def generator():
    n = int(input(Fore.BLUE + "Enter Password Length : "))
    alphabet_n = int(input(Fore.BLUE + "Enter Alphabets Length : "))
    digit_n = int(input(Fore.BLUE + "Enter Digits Length : "))
    special_n = int(input(Fore.BLUE + "Enter Special Characters Length : "))

    char_cout = alphabet_n + digit_n + special_n

    if char_cout > n:
        print(Fore.RED + "\nCharacters total count is greater than the password length\n" + Style.RESET_ALL)
        return 0
    
    password = []

    # random alphabet
    for i in range(alphabet_n):
        password.append(random.choice(alphabet))

    # random digit
    for i in range(digit_n):
        password.append(random.choice(digit))

    # random special chars
    for i in range(special_n):
        password.append(random.choice(special))

    if char_cout < n:
        random.shuffle(character)
        for i in range(n - char_cout):
            password.append(random.choice(character))

    random.shuffle(password)

    MyPassword = "".join(password)
    
    print("\n" + Fore.GREEN + MyPassword + "\n" + Style.RESET_ALL)


generator()