import random


def restart():
    while True:
        user_choice = input('Play again? "Y" or "N": ').upper()
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            return True
        else:
            print('Incorrect input. Try again')

def hit():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    new_card = random.choice(cards)
    return new_card

def blackjack_check(player, dealer):
    if sum(player) == 21 and sum(dealer) == 21:
            print("PUSH!")

    elif sum(dealer) == 21:
        print(f"Dealer blackjack! Dealer hand: {dealer}")
        
    elif sum(player) == 21:
        print("Blackjack! You won!")
        
    elif sum(player) > 21:
        print("Bust! Dealer wins!")
        
def aceFilter(user): # change 11 to 1 if sum(user) greater than 21
    try:
        aceIndex = user.index(11)
        
        if 11 in user and sum(user) > 21:
            user[aceIndex] = 1
    except ValueError:
        print()

def hand(player, dealer):
    print(f"Your cards: {player} | Current score: {sum(player)}")
    print(f"Dealer's face card: {dealer[1]} \n")

def blackjack():
    while True:
        logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """

        print(logo)

        player = []
        dealer = []

        #start game
        player.append(hit())
        player.append(hit())
        dealer.append(hit())
        dealer.append(hit())

        print(f"Your cards: {player} | Current score: {sum(player)}")
        print(f"Dealer's face card: {dealer[1]} \n")
        if sum(dealer) == 21:
            print(f"Dealer blackjack! Dealer's cards: {dealer} | score: {sum(dealer)}")
            if not restart():
                return
        
        if sum(player) == 21: # dealer hits if player get 21 on first hand
            while True:
                if sum(dealer) < 17: # dealer hit until >= 17
                    dealer.append(hit())
                    print(f"Your cards: {player} | Current score: {sum(player)}")
                    print(f"Dealer's cards: {dealer} | Current score: {sum(dealer)} \n")
                    blackjack_check(player, dealer)
                    
                elif sum(dealer) >= 17 and sum(dealer) < 21: #dealer stand after >= 17
                    print(f"Your cards: {player} | Current score: {sum(player)}")
                    print(f"Dealer's face card: {dealer} | Current score: {sum(dealer)} \n")
                    if sum(dealer) > sum(player):
                        print("Dealer wins!")
                        break
                    elif sum(dealer) < sum(player):
                        if sum(player) == 21:
                            blackjack_check(player, dealer)
                            break
            
        notGameover = True
        while notGameover:
            user_choice = input("Would you like to Hit or Stand? 'H' = Hit, 'S' = Stand: ").upper()
            if user_choice == 'H':
                player.append(hit())
                aceFilter(player)
                hand(player, dealer)
                if sum(player) == 21:
                    continue
                elif sum(player) > 21:
                    print("Bust!")
                    break

            if user_choice == 'S':
                stand = True
                while stand:
                    if sum(dealer) < 17: # dealer hit until >= 17
                        dealer.append(hit())
                        print(f"Your cards: {player} | Current score: {sum(player)}")
                        print(f"Dealer's cards: {dealer} | Current score: {sum(dealer)} \n")
                        aceFilter(dealer)
                        blackjack_check(player, dealer)
                        notGameover = False
                        break
                        
                    elif sum(dealer) >= 17 and sum(dealer) < 21: #dealer stand after >= 17
                        print(f"Your cards: {player} | Current score: {sum(player)}")
                        print(f"Dealer's face card: {dealer} | Current score: {sum(dealer)} \n")
                        if sum(dealer) > sum(player):
                            print("Dealer wins!")
                            notGameover = False
                            break

                        elif sum(dealer) < sum(player) and sum(player) == 21:
                            blackjack_check(player, dealer)
                            notGameover = False
                            break
                            
                        elif sum(dealer) < sum(player):
                            print('You win!')
                            notGameover = False
                            break
                    
                        elif sum(dealer) > 21:
                            print("Dealer bust. You've won!")
                            notGameover = False
                            break

                        elif sum(dealer) == sum(player):
                            print("Push!")
                            notGameover = False
                            break
                        
        if not restart():
            return
                            
                                      
                    
blackjack()