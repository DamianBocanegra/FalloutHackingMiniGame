#Fallout Password Crack

def addpassword(list, password):
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



def main():
    #Fill in List of Passwords
    passwords = []
    entering = True
    while entering:
        #read passwords from file
        addpassword(passwords, word)
        
    

