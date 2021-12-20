import os
import random
import shutil
import time

m1 = "01 - January"
m2 = "02 - February"
m3 = "03 - March"
m4 = "04 - April"
m5 = "05 - May"
m6 = "06 - June"
m7 = "07 - July"
m8 = "08 - August"
m9 = "09 - September"
m10 = "10 - October"
m11 = "11 - November"
m12 = "12 - December"

Dar = "/Users/username/Desktop/org"
print(os.listdir(Dar))
media_path = random.choice(os.listdir(Dar))
print(media_path)


parent_dir = "/Users/username/Desktop/hello"


os.chdir("/Users/username/Desktop/hello")
print(os.getcwd())
if media_path[5:7] == "05":
    try:
        os.makedirs(path, exist_ok=True)
        print("05 - May '%s' created successfully" % directory)
    except OSError as error:
        print("05 - May '%s' can not be created")
