import random

wordsList = ["jabłko;Logo apple", "jeansy;Spodnie Jobs'a",
         "laptop;słowo, które automatycznie wypada ze słownika w momencie zakupu macbooka",
         "arm;architektura procesora"]
letters = "a,b,c,d,f,g,h,i,j,k,l,ł,m,n,o,q,p,r,s,ś,t,u,ó,w,y,z,ź,ż"
lettersTab = letters.split(",")
knownLettersTab = []


helper1 = wordsList[random.randrange(0, 4)].split(";")
word = helper1[0]
description = helper1[1]
lifes = 5
win = False


def writeLifes():
    print("Szanse: ", end="")
    x = 0
    while x < lifes:
        print("<3 ", end="")
        x = x + 1
    print()

hiddenWord = []

def firstWord():
    for x in word:
        hiddenWord.append("_")
    for x in hiddenWord:
        print(x, end="")
    print()


def printWord(letter):
    isLetter = False
    y = 0
    for x in word:
        if x==letter:
            hiddenWord[y]=x
            isLetter = True
        y = y + 1

    for x in hiddenWord:
        print(x, end="")
    print()
    return isLetter

firstWord()
writeLifes()

while lifes > 0 and win == False:
    print(f"Podpowiedź: {description}")
    if printWord(input("Podaj literę: ").lower()):
        print("Poprawne!")
    else:
        lifes = lifes - 1
    if("".join(hiddenWord) == word):
        win = True
        print("WYGRYWASZ!")

    print()
    writeLifes()
if(win == False):
    print("Przegałeś :c")