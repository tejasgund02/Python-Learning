# Write a code for water drink reminder using python for every 1 hour. remider should speak dirck a water 2 times and then stop for 1 hour and then again speak dirck a water 2 times and then stop for 1 hour and so on


# import time
# import pyttsx3
# engine = pyttsx3.init()

# def water_reminder():
#     while True:
#         print("Time to drink water!")
#         engine.say("Time to drink water!")
#         engine.runAndWait() 
#         time.sleep(3600)  # Wait for 1 hour (3600 seconds)

# if __name__ == "__main__":
#     water_reminder()
import time
import winsound
from plyer import notification

def water_reminder():
    while True:
        # Show desktop notification
        notification.notify(
            title="💧 Water Reminder",
            message="Time to drink a glass of water!",
            timeout=10
        )

        # Play a sound alert (beep)
        # frequency = 1000 Hz, duration = 700 ms
        winsound.Beep(1000, 600)

        # Wait for 1 hour (3600 seconds)
        time.sleep(3600)

if __name__ == "__main__":
    water_reminder()
