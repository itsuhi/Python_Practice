# Problem Set 2, hangman.py
# Name: Yifei Guo
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if not char in letters_guessed:
            return False
    return True





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word = guessed_word + char
        else:
            guessed_word = guessed_word + "_ "
    return guessed_word





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    avaliable_letters = ""
    alphabet = string.ascii_lowercase
    for char in alphabet:
        if not char in letters_guessed:
            avaliable_letters = avaliable_letters + char
    return avaliable_letters

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
#    target_word = secret_word
#    unique_letters = []
#    for char in target_word:
#        if not char in unique_letters:
#            unique_letters.append(char)
#    num_unique = len(unique_letters)
#    vowels = ["a", "e", "i", "o"]
#    letters_guessed = []
#    num_of_guesses = 6
#    num_of_warnings = 3
#    length_of_word = len(target_word)
#    print("Welcome to the game of hangman!")
#    print("There are", length_of_word, "letters in the secret_word.")
#    
#    print("Avaliable letters: ", get_available_letters(letters_guessed))
#    while is_word_guessed(target_word, letters_guessed) == False and num_of_guesses > 0:
#        print("You have", num_of_warnings, "warnings left.")
#        print("You have", num_of_guesses, "guesses left")
#        print("Avaliable letters: ", get_available_letters(letters_guessed))
#        guessed_letter = input("Please guess a letter: ")
#        if str.isalpha(guessed_letter) == False:
#            if num_of_warnings > 0:
#                num_of_warnings = num_of_warnings - 1
#                print("Oops! That is not a valid letter. You have", num_of_warnings, "warnings left.")
#                print(get_guessed_word(target_word, letters_guessed))
#            else:
#                num_of_guesses = num_of_guesses - 1
#                print("Oops! That is not a valid letter. You have no warnings left. \nYou lose a guess")
#                print(get_guessed_word(target_word, letters_guessed))
#        else:
#            lower_case_letter = guessed_letter.lower()
#            if lower_case_letter in letters_guessed:
#                if num_of_warnings > 0:
#                    num_of_warnings = num_of_warnings - 1
#                    print("Oops! You have already guessed that letter. You have", num_of_warnings, "warnings left.")
#                else:
#                    num_of_guesses = num_of_guesses - 1
#                    print("Oops! You have already guessed that letter. You have no warnings left. \nYou lose a guess")
#            else:
#                letters_guessed.append(lower_case_letter)
#                if lower_case_letter in target_word:
#                    print("Good Guess!")
#                    print(get_guessed_word(target_word, letters_guessed))
#                   
#                else:
#                    if lower_case_letter in vowels:
#                        print("Try again")
#                        print(get_guessed_word(target_word, letters_guessed))
#                    
#                        num_of_guesses = num_of_guesses - 2
#                    else:
#                        print("Try again")
#                        print(get_guessed_word(target_word, letters_guessed))
#                    
#                        num_of_guesses = num_of_guesses - 1
#        print(5 * "......")
#                
#    if num_of_guesses == 0:
#        print("Game Over >.< The secret word is:", secret_word)
#    else:
#        total_score = num_of_guesses * num_unique
#        print("Congratulations! U win!! Your total score is:", total_score)
#    return ""    
#            
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    guessed_word = my_word
    edited_guessed_word = guessed_word.replace(" ", "")
    len_guessed_word= len(edited_guessed_word)
    len_otherword = len(other_word)
    hidden_letter = "_"
    if len_guessed_word == len_otherword:
        for i in range(len_otherword):
            if edited_guessed_word[i] == hidden_letter and other_word[i] in edited_guessed_word:
                return False
            
            
            if edited_guessed_word[i] != hidden_letter and edited_guessed_word[i] !=other_word[i]:
                return False
        return True
    return False
    
    




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    result = ""
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            result = result + word + " "
    if result == "":
        return "No matches found."
    else:
        return result




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    target_word = secret_word
    unique_letters = []
    for char in target_word:
        if not char in unique_letters:
            unique_letters.append(char)
    num_unique = len(unique_letters)
    vowels = ["a", "e", "i", "o"]
    letters_guessed = []
    num_of_guesses = 6
    num_of_warnings = 3
    length_of_word = len(target_word)
    print("Welcome to the game of hangman!")
    print("There are", length_of_word, "letters in the secret_word.")
    
    print("Avaliable letters: ", get_available_letters(letters_guessed))
    while is_word_guessed(target_word, letters_guessed) == False and num_of_guesses > 0:
        print("You have", num_of_warnings, "warnings left.")
        print("You have", num_of_guesses, "guesses left")
        print("Avaliable letters: ", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter: ")
        if guessed_letter == "*":
            print("Possible word matches are:")
            print(show_possible_matches(get_guessed_word(target_word, letters_guessed)))
        elif str.isalpha(guessed_letter) == False:
            if num_of_warnings > 0:
                num_of_warnings = num_of_warnings - 1
                print("Oops! That is not a valid letter. You have", num_of_warnings, "warnings left.")
                print(get_guessed_word(target_word, letters_guessed))
            else:
                num_of_guesses = num_of_guesses - 1
                print("Oops! That is not a valid letter. You have no warnings left. \nYou lose a guess")
                print(get_guessed_word(target_word, letters_guessed))
        else:
            lower_case_letter = guessed_letter.lower()
            if lower_case_letter in letters_guessed:
                if num_of_warnings > 0:
                    num_of_warnings = num_of_warnings - 1
                    print("Oops! You have already guessed that letter. You have", num_of_warnings, "warnings left.")
                else:
                    num_of_guesses = num_of_guesses - 1
                    print("Oops! You have already guessed that letter. You have no warnings left. \nYou lose a guess")
            else:
                letters_guessed.append(lower_case_letter)
                if lower_case_letter in target_word:
                    print("Good Guess!")
                    print(get_guessed_word(target_word, letters_guessed))
                   
                else:
                    if lower_case_letter in vowels:
                        print("Try again")
                        print(get_guessed_word(target_word, letters_guessed))
                    
                        num_of_guesses = num_of_guesses - 2
                    else:
                        print("Try again")
                        print(get_guessed_word(target_word, letters_guessed))
                    
                        num_of_guesses = num_of_guesses - 1
        print(5 * "......")
                
    if num_of_guesses == 0:
        print("Game Over >.< The secret word is:", secret_word)
    else:
        total_score = num_of_guesses * num_unique
        print("Congratulations! U win!! Your total score is:", total_score)
    return ""    





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
#    # pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
#    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
