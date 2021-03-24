import threading
import tkinter
from time import sleep
from tkinter import filedialog
import os
import sys
from shutil import copy2, move
import time
import pickle
from tkinter.ttk import Progressbar

root = tkinter.Tk()
root.title("Me//0W sorter pro V4")

# ## Paths###
global list_of_paths_to_offlode
list_of_paths_to_offlode = []


def offlode_list():
    list_of_paths_to_offlode.append(filedialog.askdirectory())
    updatelist()


def backup_out():
    global backup_out
    backup_out = filedialog.askdirectory()
    print(backup_out)
    change_backup_out(backup_out)


def sorter_in():
    global sorter_in
    sorter_in = filedialog.askdirectory()
    change_sorter_in(sorter_in)


def sorter_out():
    global sorter_out
    sorter_out = filedialog.askdirectory()
    change_sorter_out(sorter_out)


# ## Paths.end###

# # #On-Off# # #


def On_switchs(power_on_core):
    if power_on_core == "sorter":
        global sorter_switch
        sorter_switch = True
        change_Sorter_on()
        Sorter_core(sorter_in, sorter_out)

    if power_on_core == "offlode":
        global Offloder_switch
        Offloder_switch = True
        change_offlode_on()
        Offloder_core()

    if power_on_core == "backup":
        global backup_switch
        backup_switch = True
        change_backup_on()
        Backup_core()


def off_switchs(power_on_core):
    if power_on_core == "sorter":
        global sorter_switch
        sorter_switch = False
        change_Sorter_off()

    if power_on_core == "offlode":
        global Offloder_switch
        Offloder_switch = False
        change_offlode_off()

    if power_on_core == "backup":
        global backup_switch
        backup_switch = False
        change_backup_off()


# ##On-Off.end###

# ##save ###
def save_file_path():
    return os.path.join(sys.path[0], "Mellow_sroter_pro.dat")


def Save():
    thing_to_save_for_next_time = [
        list_of_paths_to_offlode,
        sorter_in,
        sorter_out,
        backup_out,
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
        global backup_out
        sorter_in = new_dict[1]
        sorter_out = new_dict[2]
        backup_out = new_dict[3]
        change_sorter_in(sorter_in)
        change_sorter_out(sorter_out)
        change_backup_out(backup_out)
        updatelist()
    except FileNotFoundError:
        pass

# ##save.end ###

# ##Changes to buttens###


def change_Sorter_off():
    sorter_start_stop["text"] = "start sorter"
    sorter_start_stop["command"] = lambda: [On_switchs("sorter")]


def change_offlode_off():
    start_stop_offlode["text"] = "start offlode"
    start_stop_offlode["command"] = lambda: [On_switchs("offlode")]


def change_backup_off():
    backup_start_stop["text"] = "start backup"
    backup_start_stop["command"] = lambda: [On_switchs("backup")]


def change_Sorter_on():
    sorter_start_stop["text"] = "Stop sorter"
    sorter_start_stop["command"] = lambda: [off_switchs("sorter")]


def change_offlode_on():
    start_stop_offlode["text"] = "Stop offlode"
    start_stop_offlode["command"] = lambda: [off_switchs("offlode")]


def change_backup_on():
    backup_start_stop["text"] = "Stop backup"
    backup_start_stop["command"] = lambda: [off_switchs("backup")]


def change_sorter_in(sorter_in):
    sorter_in_path["text"] = sorter_in


def change_sorter_out(sorter_out):
    sorter_out_path["text"] = sorter_out


def change_backup_out(backup_out):
    backup_out_path["text"] = backup_out


# ##Changes to buttens.end###
# ##offloder###
listbox_widget = tkinter.Listbox(
    root,
    width=30,
    height=10,
)
Add_2_offlode = tkinter.Button(
    root, height=3, width=30, text="Add path", command=offlode_list
)
start_stop_offlode = tkinter.Button(
    root,
    height=3,
    width=30,
    text="Start offlode",
    command=lambda: [On_switchs("offlode")],
)

Add_2_offlode.grid(row=1, column=0)
listbox_widget.grid(row=0, column=0)
start_stop_offlode.grid(row=2, column=0)

# ##offloder.end###

# ##sorter###
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
    text="start Sorter",
    command=lambda: [On_switchs("sorter")],
)

sorter_in_path.grid(row=5, column=0)
sorter_out_path.grid(row=6, column=0)
sorter_start_stop.grid(row=7, column=0)


def updatelist():
    listbox_widget.delete(0, tkinter.END)
    for entry in list_of_paths_to_offlode:
        listbox_widget.insert(tkinter.END, entry)


# ##sorter.end###


# ##Backup###
backup_out_path = tkinter.Button(
    root, height=3, width=30, text="(3)backup out path", command=backup_out
)
backup_start_stop = tkinter.Button(
    root,
    height=3,
    width=30,
    text="start backup",
    command=lambda: [On_switchs("backup")],
)

backup_out_path.grid(row=9, column=0)
backup_start_stop.grid(row=10, column=0)
# ##Backup.end###

Save_pre_set = tkinter.Button(
    root, height=3, width=30, text="Save", command=Save)
Save_pre_set.grid(row=12, column=0)

# ##cores###


def Sorter_core(in_path, out_path):
    print("started sorter")

    def run_sorter():
        for subdir, dirs, files in os.walk(in_path):
            progress_bar_sorter["maximum"] = len(files)
            for item in files:
                if sorter_switch is False:
                    break
                Path_2_item = os.path.join(subdir, item)

                try:
                    day = time.strftime("%d", time.localtime(
                        os.path.getmtime(Path_2_item)))

                    month = time.strftime(
                        "%B", time.localtime(os.path.getmtime(Path_2_item))
                    )

                    year = time.strftime(
                        "%Y", time.localtime(os.path.getmtime(Path_2_item))
                    )
                except FileNotFoundError:
                    pass

                day_name = day + " - " + month + " - " + year
                pathtochack = os.path.join(out_path, year, month, day_name)

                if not os.path.exists(pathtochack):
                    os.makedirs(pathtochack)

                pathtochack2 = os.path.join(pathtochack, item)
                if not os.path.exists(pathtochack2):
                    move(Path_2_item, pathtochack)
                    print(item, "copyed")
                else:
                    print(item, "exists")
                progress_bar_sorter.step()
        off_switchs("sorter")
        print("sorting Finisht")

    Sorter_thread = threading.Thread(target=run_sorter)
    Sorter_thread.start()


def Backup_core():
    def run_backup(src, dst, symlinks=False, ignore=None):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            if backup_switch is False:
                break
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                run_backup(s, d, symlinks, ignore)
            else:
                if (
                    not os.path.exists(d)
                    or os.stat(s).st_mtime - os.stat(d).st_mtime > 1
                ):
                    copy2(s, d)
                    print("copying: ", s, "to: ", d)
        off_switchs("backup")
    Backup_thread = threading.Thread(
        target=run_backup, args=(sorter_out, backup_out))
    Backup_thread.start()


def Offloder_core():
    print("startind offloding")

    def run_Offloder():
        def if_connected():
            # gets path from list
            for path in list_of_paths_to_offlode:
                # checks if the drive is conected
                if os.path.exists(path) is True:
                    # tells the offlode def drive is conected
                    offlode_card(path)
                    # passes the path
                    # off_switchs("offlode")
            print("scaning")
            sleep(5)
            if Offloder_switch is True:
                if_connected()

        # move files off sd card

        def offlode_card(sd):
            # walks the directory
            for dirName, subdirList, fileList in os.walk(sd, topdown=False):
                # progres bar staff
                # bug mathe dasent work
                filecount2 = len(dirName) + len(subdirList) + len(fileList)
                progress_bar_offloder["maximum"] = filecount2

                for fname in fileList:
                    # off switch
                    if Offloder_switch is False:
                        break
                    # comdins to path with the file name
                    # update to path.join
                    pathtofile = dirName + "/" + fname
                    pathtopop = sorter_in + "/" + fname

                    # checks if file is alredy in folder
                    if os.path.exists(pathtopop) is False:
                        print("Copying: " + fname)
                        move(pathtofile, sorter_in)
                    else:
                        print(fname + " duplcet")
                    progress_bar_offloder.step()

        if Offloder_switch is True:
            if_connected()

    Offloder_thread = threading.Thread(target=run_Offloder)
    Offloder_thread.start()


# ##cores.end###
# ## progres bar ###
progress_bar_sorter = Progressbar(root, length=270, mode="determinate")
progress_bar_sorter.grid(row=8, column=0)

progress_bar_backup = Progressbar(root, length=270, mode="determinate")
progress_bar_backup.grid(row=11, column=0)

progress_bar_offloder = Progressbar(root, length=270, mode="determinate")
progress_bar_offloder.grid(row=4, column=0)
# ## progres bar.end ###

open_save()
root.mainloop()
