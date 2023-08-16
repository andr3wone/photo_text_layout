import os

for root, dirs, files in os.walk("./photo"):
    for file in files:
        n0 = file
        n1 = ' '.join(file.split(" ")[0:-1])
        n2 = str(file.split(" ")[-1].strip(".JPG"))
import random

h = random.randint(10, 14)
m = random.randint(10, 59)
print(f"{h}:{m}")