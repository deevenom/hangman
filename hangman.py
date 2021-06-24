# program for hangman game
import random

"""we can do this in this way also
   from hangman_words import word_list
   rand_word = random.choice(word_list)"""
import hangman_art
print(hangman_art.logo)

#chosing random word
import hangman_words
rand_word = random.choice(hangman_words.word_list)
print(rand_word)
#create lives
lives = 6

#changing random word to underscore
display = []
word_length = len(rand_word)
for _ in range(word_length):
    display += '_'
print(display)

#chosing for user
#creating an exit point in game for while loop
end_of_game = 0

while not end_of_game == 1:

    guess = input("guess ur letter").lower()
    print(f"your choise is {guess}")



    if guess in display:
        print(f"you hav alredy added {guess}")

    #using for loop to check if this word is availabe in random word or not
    for position in range(word_length):#taking out latters position for rand_word
        word = rand_word[position] #taking out latter for randword according to  position
        if word == guess:
           display[position] = word
    print(display)
    #reducing lives if word is not present
    if guess not in rand_word:
        lives -= 1
        print(f"you gussed {guess}.this is not in word you lose a life.you have {lives} lives")
        if lives == 0:
            end_of_game = 1
            print("you lose")
    #using exit pont after all itration in game

    if "_" not in display:
        end_of_game = 1
        print("you won")
    #printing lives according to stage using modelus
    from hangman_art import stages
    print(stages[lives])