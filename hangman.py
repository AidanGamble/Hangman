import numpy
import os

CONST_ASCII_TO_INDEX = 65

#   Initializes game, including secret phrase, foundLetters,
#   and alreadyGuessed arrays. Also prints the initial blank
#   phrase.

def initializeGame():
    phrase = "ABCDEF"
    foundLetters = [False for i in range(len(phrase))]
    alreadyGuessed = [False for i in range(26)]
    numMisses = 5
    printRevealed(phrase, foundLetters, alreadyGuessed)
    return [phrase, foundLetters, alreadyGuessed, numMisses]

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
            print("_", end=" ")
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


def main():

    [phrase, foundLetters, alreadyGuessed, numMisses] = initializeGame()

    #Core game loop
    while((False in foundLetters) & (numMisses > 0)):
        [guessedLetter, alreadyGuessed] = parseInput(alreadyGuessed)
        if(guessedLetter in phrase):
            foundLetters = updateLetters(guessedLetter, phrase, foundLetters)
            os.system("cls")
            printRevealed(phrase, foundLetters, alreadyGuessed)
            print("Hit!")
        else:
            os.system("cls")
            printRevealed(phrase, foundLetters, alreadyGuessed)
            numMisses -= 1
            print("Miss! " + str(numMisses) + " chances left.")
        
    #Clear console before exiting
    os.system("cls")


main()