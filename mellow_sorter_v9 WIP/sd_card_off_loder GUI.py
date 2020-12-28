import datetime
import os
import threading
import tkinter as tk
from shutil import copy2
from time import sleep
from tkinter import *

top1 = Tk()
top1.title("sd")


def switchon():
    global switch
    switch = True
    print('scaning Started')
    starttimelaps()


def switchoff():
    print('scaning Stoped')
    global switch
    switch = False


def kill():
    top1.destroy()


def starttimelaps():
    def Run():
        while (switch == True):
            def path_to_drive():
                list = [
                    "/Volumes/EOS_DIGITAL/DCIM/100CANON/",
                    '/Volumes/Untitled 1/DCIM/100MEDIA/',
                ]  # SD card From canon
                return list

            # cherk if drives are connected

            def if_connected():
                # gets path from list
                for path in path_to_drive():
                    # checks if the drive is conected
                    if os.path.exists(path) == True:
                        # tells the offlode def drive is conected
                        offlode_card(path)
                        # passes the path

            # move files off sd card

            def offlode_card(sd):
                # path to the directore to move files to
                move_to = "/Volumes/WinInstall/one"
                # walks the directory
                for dirName, subdirList, fileList in os.walk(sd, topdown=False):
                    for fname in fileList:
                        # comdins to path with the file name
                        pathtofile = dirName + "/" + fname
                        pathtopop = move_to + "/" + fname
                        if os.path.exists(pathtopop) == False:
                            print("moving: " + fname)
                            copy2(pathtofile, move_to)
                        else:
                            print(fname + " duplcet")
            print("scaning")
            if_connected()
            sleep(6)

    thread = threading.Thread(target=Run)
    thread.start()


onbutton = tk.Button(top1, height=3, width=15,
                     text="Start Scaning", command=switchon)
offbutton = tk.Button(top1, height=3, width=15,
                      text="Stop scaning", command=switchoff)
killbutton = tk.Button(top1, height=3, width=15, text="EXIT",
                       command=lambda: [kill(), switchoff()])


onbutton.grid(row=11, column=0)
offbutton.grid(row=11, column=2)

killbutton.grid(row=12, column=1)

top1.mainloop()
