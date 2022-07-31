#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password():
    while True:
        print("Welcome to the PyPassword Generator!")
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        password = []

        for i in range(nr_letters):
            password.append(random.choice(letters))
        for i in range(nr_symbols):
            password.append(random.choice(symbols))
        for i in range(nr_numbers):
            password.append(random.choice(numbers))

        random.shuffle(password) #randomize password

        password = "".join(password) #combine items from list into variable

        print(f"{nr_letters} letters, {nr_symbols} symbols, {nr_numbers} numbers = {password}")
        
        if not restart():
            return
        

def restart():
    choice = input('Would you like another password? "Y" or "N" \n').upper()
    if choice == "N":
        return False
    elif choice == "Y":
        return True


password()