#Fallout Password Crack
#Recreate Fallout password cracking mini-game
import random
def addPassword(list, password):
    list.append(password)

def checkAnswer(correctPassword, guess):
    index = 0
    correctLetters = 0
    for letter in correctPassword:
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
    f = open("wordList.txt", "r")
    f1 = f.readlines()
    for x in f1:
        addPassword(passwords, x[0:len(x) - 1])
        
    return passwords

def guessPasswordsGame(passwords, correctKey):
    playing = True
    while playing:
        printPasswordList(passwords)
        playerInput = input("Select Password: ")
        correctLetters = checkAnswer(correctKey, str(playerInput))
        if correctLetters < len(correctKey):
            print("Incorrect. Letters: " + str(correctLetters) + "/" + str(len(correctKey)))
        else:
            print("SUCCESS!")
            playing = False

def main():
    #Fill in List of Passwords
    passwords = []
    play = True
    while play:
        enterPasswords(passwords)
        correctKey = passwords[random.randint(0, len(passwords) - 1)]
        print("Correct key: " + correctKey)
        guessPasswordsGame(passwords, correctKey)
        #loop is only running once for testing purposes
        play = False

main()
    

