from flask import Flask, request, jsonify
from flask import render_template
import threading
import time
import random
print("LanType Typing Website: © Lan Internet Software")
global ended
ended = False

app = Flask(__name__)
def get_word(amount=1000):
    # request code to add in the future
    with open("WORDS.JSON","r") as word:
        words = word.read().strip("[").strip("]").split(",")
        final = []
        for x in range(amount):
            final.append(random.choice(words))
        return final
def timer():
    
    with app.app_context():
        global ended
        global correct_words
        global nextword
        global incorrect
        #start timer after a prompt on the website says "And your time starts now!" after loading the words
        time.sleep(60)
        print("Time's Up!")
        ended = True
        #return render_template('results.html', score=correct_words, incorrect_words = incorrect, words=typed)
    
@app.route("/")
def mainpage():
    return render_template('lantype.html')
@app.route("/keystroke", methods=["POST"])
def get_character():
    global key_stroke
    global flag
    if request.get_json("words")["key"] != "":
        flag = True
        key_stroke = request.get_json("words")["key"][-1]
        flag = False
        return request.get_json("words")["key"][-1]
    return ""
@app.route("/get-words")
def characters():
    global typed
    typed = []
    for i in range(100):
            word = get_word()[i].replace('"',"").replace(" ","")
            typed.append( word)   
    threading.Thread(target=game).start()
    return jsonify(message=" ".join(typed))  
@app.route("/results")
def display_endpage():
    global ended
    global correct_words
    global nextword
    global incorrect
    return render_template('results.html', score=correct_words, incorrect_words = incorrect, words=typed)
def game():
    global ended
    global correct_words
    global typed
    global nextword
    global incorrect
    global key_stroke
    global flag
    key_stroke = ""
    flag = False
    correct_words = 0
    nextword = 0
    character = ""
    incorrect = {}
    threading.Thread(target=timer).start()
    while not ended:
            wordstr = ""
            while wordstr != typed[nextword]:
                if flag == True:
                    character = key_stroke
                    print("Round of a loop!")
                if character in (" "):
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
            nextword += 1              
    
                      


    


