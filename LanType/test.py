import time, threading
import msvcrt
ended = False
def timer():
    global ended
    print("And your time starts now!")
    time.sleep(3)
    print("Time's up!")
    ended = True
    exit()
threading.Thread(target=timer).start()
while ended == False:
    print(msvcrt.getwch())