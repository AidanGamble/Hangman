import numpy
import os

CONST_ASCII_TO_INDEX = 65

#   Initializes game, including secret phrase, foundLetters,
#   and alreadyGuessed arrays. Also prints the initial blank
#   phrase.

def initializeGame():
    phrase = "THIS IS SOMEONE'S TEST"
    phrase = intro(phrase).upper()
    os.system("cls")

    foundLetters = [False for i in range(len(phrase))]

    #Set found letter to true if it is not alpha
    for i in range(len(foundLetters)):
        if(not phrase[i].isalpha()):
            foundLetters[i] = True

    alreadyGuessed = [False for i in range(26)]
    numMisses = 5
    drawHangman(numMisses)
    printRevealed(phrase, foundLetters, alreadyGuessed)
    return [phrase, foundLetters, alreadyGuessed, numMisses]

def intro(phrase):
    while(True):
        x = input("Welcome to hangman! Enter '1' for singleplayer and '2' for two player: ")
        if(x == "1"):
            return phrase
        if(x == "2"):
            while(True):
                y = input("Player 1, enter your secret phrase: ")
                for i in range(len(y)):
                    if(y[i].isalpha()):
                        return y
                
                os.system("cls")
                print("Invalid entry. Phrase must have at least 1 letter.")
        else:
            os.system("cls")
            print("Invalid input.")
        
        
        

def parseInput(alreadyGuessed):
    x = input("Enter your guessed letter: ")
    if (x.isalpha() & len(x) == 1):
        if(not alreadyGuessed[ord(x.capitalize()) - CONST_ASCII_TO_INDEX]):
            alreadyGuessed[ord(x.capitalize()) - CONST_ASCII_TO_INDEX] = True
            return [x.capitalize(), alreadyGuessed]
        else:
            print("Already guessed.")
            return parseInput(alreadyGuessed)
    else:
        print("Invalid input.")
        return parseInput(alreadyGuessed)

def checkPhrase(phrase, char):
    return char in phrase

def printRevealed(phrase, foundLetters, alreadyGuessed):
    for i in range(len(phrase)):
        if(foundLetters[i]):
            print(phrase[i], end=" "),
        else:
            if(phrase[i].isalpha()):
                print("_", end=" ")
            else:
                print(phrase[i], end = " ")
    print("")
    print("Guessed Letters: ", end=" ")
    for i in range(26):
        if(alreadyGuessed[i]):
            print(chr(i + CONST_ASCII_TO_INDEX), end=" ")
        else:
            print(" ", end=" ")
    print("")



def updateLetters(letter, phrase, foundLetters):
    for i in range(len(phrase)):
        if(letter == phrase[i]):
            foundLetters[i] = True
    return foundLetters

def drawHangman(numMisses):
    print("   ____")
    print("   |  |")
    if(numMisses >= 5):
        print("   |")
    else:
        print("   |  o")
    if(numMisses >=4):
        print("   |")
    elif(numMisses >= 3):
        print("   |  |")
    elif( numMisses >= 2):
        print("   |  |\\")
    else:
        print("   | /|\\")
    if(numMisses >= 1):
        print("   |")
    else:
        print("   | / \\")
    
    print("___|___")


def main():

    [phrase, foundLetters, alreadyGuessed, numMisses] = initializeGame()

    #Core game loop
    while((False in foundLetters) & (numMisses > 0)):
        [guessedLetter, alreadyGuessed] = parseInput(alreadyGuessed)
        if(guessedLetter in phrase):
            foundLetters = updateLetters(guessedLetter, phrase, foundLetters)
            os.system("cls")
            drawHangman(numMisses)
            printRevealed(phrase, foundLetters, alreadyGuessed)
            print("Hit!")
        else:
            os.system("cls")
            numMisses -= 1
            drawHangman(numMisses)
            printRevealed(phrase, foundLetters, alreadyGuessed)
            print("Miss! " + str(numMisses) + " chances left.")
    
    if(not (False in foundLetters)):
        print("You win! Press enter to exit.")
    else:
        print("You lose! The answer was " + phrase + ". Press enter to exit.")
    
    #Blank input to wait before closing game
    y = input()
    #Clear console before exiting
    os.system("cls")


main()