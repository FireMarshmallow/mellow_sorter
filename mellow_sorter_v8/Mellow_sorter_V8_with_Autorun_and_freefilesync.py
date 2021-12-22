#   __  __      _ _               ______ _
#  |  \/  |    | | |             |  ____(_)
#  | \  / | ___| | | _____      _| |__   _ _ __ ___
#  | |\/| |/ _ \ | |/ _ \ \ /\ / /  __| | | '__/ _ \
#  | |  | |  __/ | | (_) \ V  V /| |    | | | |  __/
#  |_|  |_|\___|_|_|\___/ \_/\_/ |_|    |_|_|  \___|
#  https://www.mellowfire.com/
import os
import pickle
import sys
import time
import tkinter
from shutil import move
from tkinter import filedialog
from tkinter import *

root = tkinter.Tk()
root.title("Me//0W sorter pro V4 with autorun and freefilesync")


def sorter_in():
    global sorter_in
    sorter_in = filedialog.askdirectory()
    change_sorter_in(sorter_in)


def sorter_out():
    global sorter_out
    sorter_out = filedialog.askdirectory()
    change_sorter_out(sorter_out)


def ask_backup_file():
    global backup_file_path
    backup_file_path = filedialog.askopenfilename()
    print(backup_file_path)
    change_backup_name(backup_file_path)


def On_switchs(power_on_core):
    if power_on_core == "sorter":
        global sorter_switch
        global backup_file_path
        sorter_switch = True
        change_Sorter_on()
        Sorter_core(sorter_in, sorter_out)


def off_switchs(power_on_core):
    if power_on_core == "sorter":
        global sorter_switch
        sorter_switch = False
        change_Sorter_off()


def save_file_path():
    return os.path.join(sys.path[0], "Mellow_sroter_V8.dat")


def Save():
    thing_to_save_for_next_time = [
        sorter_in,
        sorter_out,
        backup_file_path,
    ]
    with open(save_file_path(), "wb") as outfile:
        pickle.dump(thing_to_save_for_next_time, outfile)


def open_save():
    try:
        with open(save_file_path(), "rb") as infile:
            new_dict = pickle.load(infile)
        global sorter_in
        global sorter_out
        global backup_file_path
        sorter_in = new_dict[0]
        sorter_out = new_dict[1]
        backup_file_path = new_dict[2]
        change_sorter_in(sorter_in)
        change_sorter_out(sorter_out)
        change_backup_name(backup_file_path)
    except FileNotFoundError:
        pass


def change_Sorter_off():
    sorter_start_stop["text"] = "Start sorter"
    sorter_start_stop["command"] = lambda: [On_switchs("sorter")]


def change_Sorter_on():
    sorter_start_stop["text"] = "Stop sorter"
    sorter_start_stop["command"] = lambda: [off_switchs("sorter")]


def change_sorter_in(sorter_in):
    sorter_in_path["text"] = sorter_in


def change_sorter_out(sorter_out):
    sorter_out_path["text"] = sorter_out


def change_backup_name(backup_file_path):
    back_up_file["text"] = backup_file_path


sorter_in_path = tkinter.Button(
    root, height=3, width=30, text="(1)Sorter in path", command=sorter_in
)
sorter_out_path = tkinter.Button(
    root, height=3, width=30, text="(2)Sorter out path", command=sorter_out
)
back_up_file = tkinter.Button(
    root, height=3, width=30, text="(3)Select the .ffs_batch", command=ask_backup_file
)


sorter_start_stop = tkinter.Button(
    root,
    height=3,
    width=30,
    text="Start sorter",
    command=lambda: [On_switchs("sorter")],
)

box = IntVar()
c = Checkbutton(root, text="AutoRun Ever hour", variable=box)

sorter_in_path.grid(row=5, column=0)
sorter_out_path.grid(row=6, column=0)
back_up_file.grid(row=7, column=0)
sorter_start_stop.grid(row=8, column=0)
Save_pre_set = tkinter.Button(root, height=3, width=30, text="Save", command=Save)
Save_pre_set.grid(row=12, column=0)
c.grid(row=13, column=0)


def run_backup(batchrun):
    os.system("FreeFileSync " + batchrun)


def Sorter_core(in_path, out_path):
    for subdir, dirs, files in os.walk(in_path):
        for item in files:
            Path_2_item = os.path.join(subdir, item)
            try:
                day = time.strftime("%d", time.localtime(os.path.getmtime(Path_2_item)))

                monthname = time.strftime(
                    "%B", time.localtime(os.path.getmtime(Path_2_item))
                )

                monthnom = time.strftime(
                    "%m", time.localtime(os.path.getmtime(Path_2_item))
                )
                month = monthnom + " - " + monthname

                year = time.strftime(
                    "%Y", time.localtime(os.path.getmtime(Path_2_item))
                )
            except FileNotFoundError:
                pass

            day_name = day + " - " + monthnom + " - " + year
            pathtochack = os.path.join(out_path, year, month, day_name)

            if not os.path.exists(pathtochack):
                os.makedirs(pathtochack)

            pathtochack2 = os.path.join(pathtochack, item)
            if not os.path.exists(pathtochack2):
                try:
                    move(Path_2_item, pathtochack)
                    print(item, "copyed")
                except:
                    print(item, "exists")

    off_switchs("sorter")
    print("sorting Finisht")
    run_backup(backup_file_path)
    if box.get() == 1:
        time.sleep(3600)
        print("loop")
        On_switchs("sorter")


open_save()
root.mainloop()
