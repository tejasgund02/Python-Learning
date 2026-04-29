import time




print("Current time in seconds since the epoch:", time.time())
print("Current local time:", time.localtime())
print("Current time in a human-readable format:", time.asctime())
print("Current time in a human-readable format using strftime:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))