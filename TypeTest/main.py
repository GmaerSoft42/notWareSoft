import time
import datetime
import threading
import requests
import os
import random
import msvcrt
import sys
ended = False
def get_word(amount=1000):
    # request code to add in the future
    with open("WORDS.JSON","r") as word:
        words = word.read().strip("[").strip("]").split(",")
        final = []
        for x in range(amount):
            final.append(random.choice(words))
        return final
def timer():
    global incorrect
    global ended
    global correct_words
    print("And your time starts now!")
    time.sleep(60)
    print("Time's up!")
    ended = True #True
    print(f"You have managed to do {correct_words}WPM")
    print(f"Incorrect words: {incorrect}")
def game():
    global increment
    increment = 0
    typed = get_word()[increment].replace('"',"").replace(" ","")
    while not ended:
        print('')
        print(f"Type the word: {typed}")
        print('')
        word = input("Type the word shown. When ready, strike ENTER: ").strip("\n")
        print('')
        if word == typed:
            increment += 1
            typed = get_word()[increment].replace('"',"").replace(" ","")
            print("Correct! Here is your next word")
        else:
            print("Incorrect! Please try again")
def game2():
    global correct_words
    correct_words = 0
    nextword = 0
    character = ""
    typed = []
    global incorrect
    incorrect = {}
    for i in range(100):
            word = get_word()[i].replace('"',"").replace(" ","")
            typed.append( word)
    print("Type the following: " + " ".join(typed))
    while not ended:
        wordstr = ""
        while wordstr != typed[nextword]:
            character = msvcrt.getwch()
            if character == '\x08':
                wordstr = wordstr[:-1]
                print('\b \b', end='', flush=True)
            elif character in ('\r', '\n',):
                pass
            elif character in (" "):
                print(character, end='', flush=True)
                if wordstr != typed[nextword-1] and wordstr != "":
                    incorrect[typed[nextword-1]] = wordstr
                elif wordstr != "":
                    correct_words += 1
                break
            else:
                print(character, end='', flush=True)
                wordstr += character
                if wordstr == typed[nextword]:
                    correct_words += 1
        print('',end='')
        nextword += 1
threading.Thread(target=timer).start()
game2()





