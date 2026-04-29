# I want shoutout to me for doing this project
# I want to convert text to speech using pyttsx3 module 
import pyttsx3
engine = pyttsx3.init()
l = ["Tejas", "Om", "python"]
for i in l:
    # engine.say(i)
    print(i)
    text = f"Very good work {i}! Keep it up boy! You are doing great! I'm proud of you!"
    engine.say(text)
    engine.runAndWait()