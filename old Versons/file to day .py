import os
import random
import shutil
import time


i = 1
while i < (2000):
    Dar = "/Users/username/Desktop/drophere"
    dir = os.listdir(Dar)

    os.chdir(Dar)
    media_path = random.choice(os.listdir(Dar))
    created = os.stat(media_path).st_ctime
    modificationTime = time.strftime(
        "%d - %m - %Y", time.localtime(os.path.getmtime(media_path))
    )
    print(media_path)
    print(modificationTime)
    os.chdir("/Users/username/Desktop/org/")
    if not os.path.exists(modificationTime):
        os.makedirs(modificationTime)
    original = "/Users/username/Desktop/drophere/" + str(media_path)
    target = "/Users/username/Desktop/org/" + str(modificationTime)
    shutil.move(original, target)
    print("goodbye")
    i += 1
print("complite")
