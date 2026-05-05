# Write a code for water drink reminder using python for every 1 hour. remider should speak dirck a water 2 times and then stop for 1 hour and then again speak dirck a water 2 times and then stop for 1 hour and so on


import time
import pyttsx3
engine = pyttsx3.init()

def water_reminder():
    while True:
        print("Time to drink water!")
        engine.say("Time to drink water!")
        engine.runAndWait() 
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)

if __name__ == "__main__":
    water_reminder()