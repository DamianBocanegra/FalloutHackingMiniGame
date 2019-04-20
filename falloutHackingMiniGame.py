#Fallout Password Crack
#Recreate Fallout password cracking mini-game
import random
def addPassword(list, password):
    list.append(password)

def checkAnswer(correctPassword, guess):
    for letter in correctPassword:
        correctLetters = 0
        index = 0
        if guess[index] != letter:
            index += 1
        else:
            index += 1
            correctLetters += 1
        return correctLetters

def printPasswordList(list):
    for word in list:
        print(word)

def enterPasswords(passwords):
    entering = True
    while entering:
        word = raw_input("Please enter password: ")
        if word != "0":
            addPassword(passwords, word)
        else:
            entering = False
    return passwords

def guessPasswordsGame(passwords, correctKey):
    playing = True
    while playing:
        printPasswordList(passwords)
        playerInput = raw_input("Select Password: ")
        correctLetters = checkAnswer(correctKey, playerInput)
        if correctLetters < len(correctKey):
            print("Incorrect. Letters: " + corrrectLetters + "/" + len(correctKey))
        else:
            print("SUCCESS!")

def main():
    #Fill in List of Passwords
    passwords = []
    play = True
    while play:
        enterPasswords(passwords)
        correctKey = passwords[random.randint(0, len(passowrds) - 1)]
        guessPasswordsGame(passwords, correctKey)
        #loop is only running once for testing purposes
        play = False
        
    

