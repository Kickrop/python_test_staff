from datetime import datetime
import time
import random

odds = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19,
        21,23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,53,55,57,59 ]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print ("this minute seems a little odd.")
    else:
        print("not an odd minute")
    odd_pouse = random.randint(1,5)
    time.sleep(odd_pouse)
    print ("you've been waiting for " + str(odd_pouse) + " seconds")
