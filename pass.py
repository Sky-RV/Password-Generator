import string
import random
import os
from colorama import Fore, Style

os.system('cls' or 'clear')
print(Style.RESET_ALL)

print(Fore.YELLOW + "GENERATE PASSWORD \n")

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate():
    n = int(input(Fore.BLUE + "Enter Password Length : "))

    random.shuffle(characters)
    password = []

    for i in range(n):
        password.append(random.choice(characters))

    random.shuffle(password)
    MyPassword = "".join(password)
    
    print("\n" + Fore.GREEN + MyPassword + "\n" + Style.RESET_ALL)

generate()