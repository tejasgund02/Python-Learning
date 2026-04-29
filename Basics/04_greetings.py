import time

t= time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if (hour>0 and hour<12):
    print("Good Morning Om")
elif (hour>12 and hour<16):
    print("Good Afternoon Om")
elif (hour>16 and hour<20):
    print("Good Evening Om")
else:
    print("Good Night Om")