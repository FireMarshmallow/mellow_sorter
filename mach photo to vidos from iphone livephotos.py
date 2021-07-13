import os
from shutil import move
import time

#test paths
heic = "/Volumes/SSD_1T/amys/HEIC iphone photos"
vids = "/Volumes/SSD_1T/amys/vidos"
live = '/Volumes/SSD_1T/amys/live photos'

#loop throw the photos folder 
for subdir, dirs, files in os.walk(heic):
    for photo in files:
        vido_name = photo.replace('.HEIC', '.mov')
        vido_path = os.path.join(vids, vido_name)
        photo_path = os.path.join(heic, photo)
        if os.path.exists(os.path.join(vids, vido_name)):
            move(photo_path, live)
            move(vido_path, live)
            print(vido_path)
            print(photo_path)
        else:
            print('no')





#check if file exists 

#move both files to live photos
