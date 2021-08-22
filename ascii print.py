import os
import time
file = open("E:/open.txt", "r")
lines = file.readlines()
print("~~printing~~")
os.system('cls')
for line in lines:
    print(line)
    time.sleep(0.3)