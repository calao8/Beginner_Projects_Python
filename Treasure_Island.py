
def restart():
    while True:
        user_choice = input('Would you like to play again? "Y" or "N" \n').lower()
        if user_choice == 'n':
            return False
        elif user_choice == 'y':
            return True
        else:
            print('Try again')

def game():
    while True:
        print('''
        *******************************************************************************
                |                   |                  |                     |
        _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
        _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        ''')
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.") 


        choice = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": ').lower()
        if choice == "right":
            print("Fall into a hole. Game over.")
            if not restart():
                return
        elif choice == "left": 
            choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
            if choice == "swim":
                print("Attacked by trout. Game Over.")
                if not restart():
                    return
            elif choice == "wait":
                choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: ").lower()
                if choice == "red":
                    print("You have been burned by fire. Game Over.")
                    if not restart():
                        return
                elif choice == "yellow":
                    print("You win!")
                    if not restart():
                        return
                elif choice == "blue":
                    print('Eaten by beasts. Game Over.')
                    if not restart():
                        return
                else:
                    print("Game Over.")
                    if not restart():
                        return
        else:
            print("Wrong answer. Try again.")
    



game()