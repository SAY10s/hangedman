from random import random

words = ["jabłko;Logo apple", "jeansy;Spodnie Jobs'a",
         "laptop;słowo, które automatycznie wypada ze słownika w momencie zakupu macbooka",
         "ARM;architektura procesora"]

nick = input("Podaj swój nick: ")
print(words[random()*3])
print(f"Witaj {nick}!")
