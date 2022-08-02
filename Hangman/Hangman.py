import random
from words import words
import string


def valid_word(words): #gets word w/o containing sym or spaces
    chosen_word = random.choice(words) #gets random word
    while '-' in chosen_word or ' ' in chosen_word:
        chosen_word = random.choice(words)
    
    return chosen_word.lower()


def hangman():
    chosen_word = valid_word(words)
    word_letters = set(chosen_word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'You have {lives} lives and you have used these letters: {"".join(used_letters)} \n')
        
        # show the current progress of the word (ie W--S-A-E) 
        word_list = [letter if letter in used_letters else '-' for letter in chosen_word] 
        print(f'Current word: {" ".join(word_list)}')

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print('Letter is not in word.\n')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.\n')

        else:
            print('Invalid character. Please try again.\n')
    
    # gets here when len(word_letters) == 0 OR when lives == 0 
    if lives == 0:
        print(f'Out of lives. The word was {chosen_word}')
    else:
        print(f'You guessed the word: {chosen_word}!!')
    

hangman()
