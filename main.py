from gpiozero import Button
from signal import pause
import gpiozero
import threading
import time
from discord_noti import send_output
from cooldown_check import can_run

btn = Button(2) 

#this class handles the status of the door  
class doorStatus:
    def __init__(self):
        self.status = "unknown"
        self.last_change = 0
        self.open_alert_sent = False

#this class handles the last printed output of the door 
class doorLastPrint:
    def __init__(self):
        self.status = "unknown"
        self.last_change = 0
        
door = doorStatus() #only need one global object (instance) of the class above, so it is updated and can be checked
lastPrint = doorLastPrint()

#callback functions
def door_closed():
    door.status = "closed" #keeps track of the door status
    door.last_change = time.time()
    if can_run("door_closed", 7): #from cooldown_check.py
        lastPrint.status = "closed" #keeps track of the last output
        lastPrint.last_change = time.time()
        door.open_alert_sent = False
        print(f"your door was {door.status} sir", time.strftime("%I:%M:%S %p")) #THIS WILL BE REPLACED WITH THE APPROPRIATE OUTPUT FUNCTION
        send_output(f"your door was {door.status} sir", time.strftime("%I:%M:%S %p")) #discord
    
def door_opened():
    door.status = "opened" #keeps track of the door status
    door.last_change = time.time()
    if can_run("door_opened", 7): #from cooldown_check.py
        lastPrint.status = "opened" #keeps track of the last output
        lastPrint.last_change = time.time()
        print(f"your door was {door.status} sir", time.strftime("%I:%M:%S %p")) #THIS WILL BE REPLACED WITH THE APPROPRIATE OUTPUT FUNCTION
        send_output(f"your door was {door.status} sir", time.strftime("%I:%M:%S %p")) #discord

#attributes that check the btn state to then handle callback functions 
btn.when_pressed = door_closed 
btn.when_released = door_opened 


#this function runs in the background and lets me know if my door has been opened for too long
def open_noti():
    while True:
        now=time.time()
        if door.status == "opened" and not door.open_alert_sent and (now - door.last_change) >= 300:
            print(f"some nga left your door {door.status} for 5 min", time.strftime("%I:%M:%S %p"))
            send_output(f"your door was left {door.status} for 5 min sir", time.strftime("%I:%M:%S %p")) #discord
            door.open_alert_sent = True #avoids it from spamming this alert once 5 min door open is true 
        time.sleep(0.5)  # check twice per second
threading.Thread(target=open_noti, daemon=True).start()


#this checks if the actual door status is accurately represtned by the outputed status (they're not the same because of the cooldown which is in place to prevent spam)
def reconcile_print():
    while True:
        now = time.time()
        if door.status != lastPrint.status and (now - lastPrint.last_change) >= 8:
            lastPrint.status = door.status
            lastPrint.last_change = now
            print(f"some nga {door.status} your door", time.strftime("%I:%M:%S %p"))
            send_output(f"some nga {door.status} your door", time.strftime("%I:%M:%S %p")) #discord
        time.sleep(0.5)  # check twice per second
#Without threading, the program would get stuck inside reconcile_print() forever.
#With threading, reconcile_print() runs forever in the background, while the rest of the program continues normally.

threading.Thread(target=reconcile_print, daemon=True).start()
pause() 

#what to add
#dashboard (webpage) 