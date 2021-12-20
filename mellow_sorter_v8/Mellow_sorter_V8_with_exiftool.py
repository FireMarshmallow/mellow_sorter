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
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.title("Me//0W sorter With exiftool")

global list_of_paths_to_offlode
list_of_paths_to_offlode = []


def sorter_in():
    global sorter_in
    sorter_in = filedialog.askdirectory()
    change_sorter_in(sorter_in)


def sorter_out():
    global sorter_out
    sorter_out = filedialog.askdirectory()
    change_sorter_out(sorter_out)


def On_switchs(power_on_core):
    if power_on_core == "sorter":
        global sorter_switch
        sorter_switch = True
        change_Sorter_on()
        Sorter_core(sorter_in, sorter_out)


def off_switchs(power_on_core):
    if power_on_core == "sorter":
        global sorter_switch
        sorter_switch = False
        change_Sorter_off()


def save_file_path():
    return os.path.join(sys.path[0], "Mellow_sroter_pro.dat")


def Save():
    thing_to_save_for_next_time = [
        list_of_paths_to_offlode,
        sorter_in,
        sorter_out,
    ]
    with open(save_file_path(), "wb") as outfile:
        pickle.dump(thing_to_save_for_next_time, outfile)


def open_save():
    try:
        with open(save_file_path(), "rb") as infile:
            new_dict = pickle.load(infile)
        for item in new_dict[0]:
            list_of_paths_to_offlode.append(item)
        global sorter_in
        global sorter_out
        sorter_in = new_dict[1]
        sorter_out = new_dict[2]
        change_sorter_in(sorter_in)
        change_sorter_out(sorter_out)
        # updatelist()
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


sorter_in_path = tkinter.Button(
    root, height=3, width=30, text="(1)Sorter in path", command=sorter_in
)
sorter_out_path = tkinter.Button(
    root, height=3, width=30, text="(2)Sorter out path", command=sorter_out
)
sorter_start_stop = tkinter.Button(
    root,
    height=3,
    width=30,
    text="Start sorter",
    command=lambda: [On_switchs("sorter")],
)

sorter_in_path.grid(row=5, column=0)
sorter_out_path.grid(row=6, column=0)
sorter_start_stop.grid(row=7, column=0)
Save_pre_set = tkinter.Button(root, height=3, width=30, text="Save", command=Save)
Save_pre_set.grid(row=12, column=0)


def Sorter_core(in_path, out_path):
    for subdir, dirs, files in os.walk(in_path):
        if ".DS_Store" in files:
            files.remove(".DS_Store")
        for item in files:
            Path_2_item = os.path.join(subdir, item)
            try:
                with exiftool.ExifTool() as e:
                    metadata = e.get_metadata(Path_2_item)
                    exifdate = metadata["QuickTime:MediaCreateDate"]
                    months_nom = [
                        "thisisnothint",
                        "01 - January",
                        "02 - February",
                        "03 - March",
                        "04 - April",
                        "05 - may",
                        "06 - June",
                        "07 - July",
                        "08 - August",
                        "09 - September",
                        "10 - October",
                        "11 - November",
                        "12 - December",
                    ]

                    year = exifdate[:4]
                    day = exifdate[8:10]
                    month = exifdate[5:7]
                    month_text = months_nom[int(month)]

            except FileNotFoundError:
                pass

            day_name = day + " - " + month + " - " + year
            pathtochack = os.path.join(out_path, year, month_text, day_name)

            if not os.path.exists(pathtochack):
                os.makedirs(pathtochack)

            pathtochack2 = os.path.join(pathtochack, item)
            if not os.path.exists(pathtochack2):
                try:
                    move(Path_2_item, pathtochack)
                    print(item, "copyed")
                except:
                    print(item, "exists")
    # off_switchs("sorter")
    print("sorting Finisht")


open_save()
root.mainloop()
