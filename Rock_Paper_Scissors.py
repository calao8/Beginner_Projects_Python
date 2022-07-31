import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def game():
    while True:

        hand = [rock, paper, scissors]
    
        while True: #loop until user input valid int
            try:
                user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
                if user_choice in range(0, len(hand)):
                    break
                elif user_choice not in range(0, len(hand)):
                    print('Invalid input. Try again.')
            except ValueError:
                print('Not a valid integer. Please Try again')

        print(hand[user_choice]) #prints the selected hand

        computer_choice = random.randint(0, len(hand) - 1)

        if computer_choice == user_choice:
            print("Computer chose: ")
            print(hand[computer_choice])
            print('Tie game \n')
            if not restart():
                return
        elif computer_choice == 0 and user_choice == 1 or computer_choice == 1 and user_choice == 2 or computer_choice == 2 and user_choice == 0:
            print("Computer chose: ")
            print(hand[computer_choice])
            print('You win! \n')
            if not restart():
                return
        elif computer_choice == 0 and user_choice == 2 or computer_choice == 1 and user_choice == 0 or computer_choice == 2 and user_choice == 1:
            print("Computer chose: ")
            print(hand[computer_choice])
            print('You lose! \n')
            if not restart():
                return


def restart():
    while True:
        user_choice = input('Play again? "Y" or "N" \n').upper()
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            return True
        else:
            print('Incorrect input. Try again')


game()