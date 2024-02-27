import random
from words import word_list

def draw_hangman(chances):
    if chances == 6:
        print("________ ")
        print("|  | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 5:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 4:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| / ")
        print("| ")
        print("| ")
    elif chances == 3:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\\ ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\\ ")
        print("| / ")
        print("| ")
    elif chances == 0:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\\ ")
        print("| / \\ ")
        print("| ")

# fills in the guessed letter
def updateWord(letter, guessed_word, word): 
    lst = list(guessed_word)
    for i in range(len(word)):
        if letter == word[i]:
            lst[i*2] = letter
    return ''.join(lst)

def playHangMan(word):
    used_letters = []
    guessed_word = '_ ' * len(word)
    tries_left = 6
    guessed = False
    
    while not guessed and tries_left > 0:
        print('\nYou have', tries_left,  'tries left.\nUsed letters: ', *used_letters, '\nWord: ', guessed_word)
        draw_hangman(tries_left)

        letter = input("\nGuess a letter: ").lower()

        if(len(letter) == 1 and letter.isalpha()):
            if letter + ' ' in used_letters:
                print(f"\nYou already guessed {letter}")
            elif letter in word:
                guessed_word = updateWord(letter, guessed_word, word)
                used_letters.append(letter + ' ')
            else:
                tries_left = tries_left - 1
        else: # if the guess is not a letter
            print("Your guess is invalid!")

        if '_' not in guessed_word:
            guessed = True

    if guessed:
        print(f"\nYay! You guessed the word {word}!\n")
    else:
        draw_hangman(tries_left)
        print(f"\nOops! No more tries left, the correct word is {word}!\n")

def main():
    playHangMan(random.choice(word_list).lower())

    while input("Play Again? (Y/N) ").upper() == "Y":
        playHangMan(random.choice(word_list).lower())

if __name__ == "__main__":
    main()