# rename the file whose ends with txt to md using for loop
import os
print(os.listdir()) 
for filename in os.listdir():
    if filename.endswith(".md"):
        new_filename = filename[:-3] + ".txt"
        os.rename(filename, new_filename)
