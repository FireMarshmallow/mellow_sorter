import os
import shutil
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import csv
import sys
import pickle

root = Tk()
root.title("Me//0W sorter V8.1")
path = "."


def folder1():
    global folder_selected1
    folder_selected1 = filedialog.askdirectory()


def folder2():
    global folder_selected2
    folder_selected2 = filedialog.askdirectory()


#save############


def save_file_path():
    PathAndName = os.path.join(sys.path[0], "mellow_sorter_save.dat")
    return PathAndName


def Save(folder_selected1, folder_selected2):
    thing_to_save_for_next_time = [
        folder_selected1,
        folder_selected2,
    ]
    outfile = open(save_file_path(), "wb")
    pickle.dump(thing_to_save_for_next_time, outfile)
    outfile.close()


def open_save():
    try:
        infile = open(save_file_path(), "rb")
        new_dict = pickle.load(infile)
        infile.close()
        global folder_selected2
        global folder_selected1
        folder_selected1 = new_dict[0]
        folder_selected2 = new_dict[1]
        changeText1()
        changeText2()
    except:
        pass

##############


def Run():
    path = folder_selected1
    for subdir, dirs, files in os.walk(path):
        path = folder_selected1
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        for file in files:
            progress['maximum'] = len(files)
            try:
                this = os.path.join(subdir, file)
                modificationTime = time.strftime(
                    '%d', time.localtime(os.path.getmtime(this)))
                modificationTime1 = time.strftime(
                    '%m', time.localtime(os.path.getmtime(this)))
                modificationTime2 = time.strftime(
                    '%Y', time.localtime(os.path.getmtime(this)))
            except:
                print('Cant find date')
            os.chdir(folder_selected2)
            dayFolder = modificationTime+' - '+modificationTime1+' - '+modificationTime2
            if not os.path.exists(modificationTime2):
                os.makedirs(modificationTime2)
            os.chdir(folder_selected2+'/'+modificationTime2)
            months_nom = ['00-IgotLazy', '01 - January', '02 - February', '03 - March', '04 - April', '05 - May',
                          '06 - June', '07 - July', '08 - August', '09 - September', '10 - October', '11 - November', '12 - December']
            if not os.path.exists(months_nom[int(modificationTime1)]):
                os.makedirs((months_nom[int(modificationTime1)]))
            os.chdir(folder_selected2+'/'+modificationTime2 +
                     '/'+months_nom[int(modificationTime1)])
            if not os.path.exists(dayFolder):
                os.makedirs(dayFolder)
            os.chdir(folder_selected2+'/'+modificationTime2 +
                     '/'+months_nom[int(modificationTime1)])
            if not os.path.exists(file):
                try:
                    shutil.copy2(this, dayFolder)
                    print(file, 'moved')
                except:
                    print('cant move', file)
            else:
                print(file, 'exists')
            progress.step()
            root.update()
        print('Done')


def Undo():
    def doit():
        for subdir, dirs, files in os.walk(folder_selected2):
            os.chdir(subdir)
            for file in files:
                try:
                    shutil.copy2(file, folder_selected1)
                except:
                    print('nope')
        kill()

    def kill():
        top.destroy()

    top = Toplevel()
    top.title("Undo")
    warning = Label(top, text='!WARNING!')
    warning.grid(row=0, column=1)
    undoworning = Label(top, text='This will put all the files into')
    undoworning.grid(row=1, column=1)
    woringfolder = Label(top, text=folder_selected1)
    woringfolder.grid(row=2, column=1)
    nosub = Label(top, text='With NO sub folders')
    nosub.grid(row=3, column=1)
    undoconfarm = Button(top, text='continue', command=doit)
    undoconfarm.grid(row=4, column=1)

    button = Button(top, text="Dismiss", command=kill)
    button.grid(row=5, column=1)


def changeText1():
    Button1['text'] = folder_selected1


def changeText2():
    Button2['text'] = folder_selected2


Button0 = tk.Button(root, text="Save", activeforeground="blue",
                    height=5, width=50, command=lambda: [Save(folder_selected1, folder_selected2)])
Button0.pack()

progress = Progressbar(root, orient=HORIZONTAL,
                       length=450, mode='determinate')
Button1 = tk.Button(root, text="Select input folder", activeforeground="blue",
                    height=5, width=50, command=lambda: [folder1(), changeText1()])
Button1.pack()
Button2 = tk.Button(root, text="Select output folder", activeforeground="blue",
                    height=5, width=50, command=lambda: [folder2(), changeText2()])
Button2.pack()
Button3 = tk.Button(root, text="Run Me//0W sorter",
                    activeforeground="green", height=5, width=50, command=Run)
Button3.pack()
Button4 = tk.Button(root, bg='black', text="UNDO",
                    activeforeground="red", height=5, width=50, command=Undo)
Button4.pack()
progress.pack()
open_save()
root.mainloop()
