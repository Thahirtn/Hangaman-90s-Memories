import random

hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  |  ===""", """
+---+
  | |
  O |
 /|\|
 /|\ ===""", """
 
""" 
               ]

Marvel_characters = ['thor', 'hulk', 'captain america', 'iron man', 'black widow', 'loki', 'spiderman', 'wanda']

word = random.choice(Marvel_characters).lower()

guessed_correctly = []
guessed_incorrectly= []
tries = 6
hangman_count = -1
while tries > 0:
    output = ''
    for letter in word:
        if letter is guessed_correctly:
            output += letter
        else:
            output += '_ '
    if output==word:
        break

    print("Guess the word: ",output)
    print(tries," chances left")  
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in word:
        print("Awesome job! You guessed a correct letter!")
    else:
        print("sorry! You have guessed a wrong letter!")
        hangman_count = hangman_count +1
        tries = tries -1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])

if tries >0:
    print("You guessed it right and you win!!! ")
else:
    print("sorry you guessed the letter. Try again.")   

    
 


    







