import threading
import tkinter as tk
from tkinter import *
from time import sleep
from tkinter import filedialog
import os
import sys
from shutil import copy2, move
import time
import pickle
from tkinter.ttk import Progressbar

root = Tk()
root.title("Me//0W sorter pro")

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
        Backup_core(sorter_out, backup_out)


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
    PathAndName = os.path.join(sys.path[0], "Mellow_sroter_pro.dat")
    return PathAndName


def Save():
    thing_to_save_for_next_time = [
        list_of_paths_to_offlode,
        sorter_in,
        sorter_out,
        backup_out,
    ]
    outfile = open(save_file_path(), "wb")
    pickle.dump(thing_to_save_for_next_time, outfile)
    outfile.close()


def open_save():
    try:
        infile = open(save_file_path(), "rb")
        new_dict = pickle.load(infile)
        infile.close()
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
    except:
        pass
# ##save.end ###

# ##Changes to buttens###


def change_Sorter_off():
    sorter_start_stop["text"] = "start sorter"
    sorter_start_stop["command"] = lambda: [On_switchs("sorter")]


def change_offlode_off():
    start_stop_offlode["text"] = "start offlode"
    start_stop_offlode["command"] = lambda: [On_switchs("offlode")]
    pass


def change_backup_off():
    backup_start_stop["text"] = "start backup"
    backup_start_stop["command"] = lambda: [On_switchs("backup")]


def change_Sorter_on():
    sorter_start_stop["text"] = "Stop sorter"
    sorter_start_stop["command"] = lambda: [off_switchs("sorter")]


def change_offlode_on():
    start_stop_offlode["text"] = "Stop offlode"
    start_stop_offlode["command"] = lambda: [off_switchs("offlode")]
    pass


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
listbox_widget = tk.Listbox(root, width=30, height=10,)
Add_2_offlode = tk.Button(root, height=3, width=30,
                          text='Add path', command=offlode_list)
start_stop_offlode = tk.Button(
    root, height=3, width=30, text='Start offlode', command=lambda: [On_switchs("offlode")])

Add_2_offlode.grid(row=1, column=0)
listbox_widget.grid(row=0, column=0)
start_stop_offlode.grid(row=2, column=0)

# ##offloder.end###

# ##sorter###
sorter_in_path = tk.Button(root, height=3, width=30,
                           text='(1)Sorter in path', command=sorter_in)
sorter_out_path = tk.Button(root, height=3, width=30,
                            text='(2)Sorter out path', command=sorter_out)
sorter_start_stop = tk.Button(root, height=3, width=30,
                              text='start Sorter', command=lambda: [On_switchs("sorter")])

sorter_in_path.grid(row=5, column=0)
sorter_out_path.grid(row=6, column=0)
sorter_start_stop.grid(row=7, column=0)


def updatelist():
    listbox_widget.delete(0, tk.END)
    for entry in list_of_paths_to_offlode:
        listbox_widget.insert(tk.END, entry)

# ##sorter.end###


# ##Backup###
backup_out_path = tk.Button(root, height=3, width=30,
                            text='(3)backup out path', command=backup_out)
backup_start_stop = tk.Button(root, height=3, width=30,
                              text='start backup', command=lambda: [On_switchs("backup")])

backup_out_path.grid(row=9, column=0)
backup_start_stop.grid(row=10, column=0)
# ##Backup.end###

Save_pre_set = tk.Button(root, height=3, width=30,
                         text='Save', command=Save).grid(row=12, column=0)

# ##cores###


def Sorter_core(in_path, out_path):
    def run_sorter():
        for subdir, dirs, files in os.walk(in_path):
            progress_bar_1['maximum'] = len(files)
            for item in files:
                if sorter_switch == False:
                    break
                Path_2_item = os.path.join(subdir, item)
                try:
                    day = time.strftime(
                        '%d', time.localtime(os.path.getmtime(Path_2_item)))
                    month = time.strftime(
                        '%B', time.localtime(os.path.getmtime(Path_2_item)))
                    year = time.strftime(
                        '%Y', time.localtime(os.path.getmtime(Path_2_item)))
                except:
                    print('Cant find date')
                day_name = day+' - '+month+' - '+year
                pathtochack = out_path+'/'+year+'/'+month+'/'+day_name
                if not os.path.exists(pathtochack):
                    os.makedirs(pathtochack)
                if not os.path.exists(item):
                    try:
                        move(Path_2_item, pathtochack)
                        print(item, 'copyed')
                    except:
                        print('cant copy', item)
                else:
                    print(item, 'exists')
                progress_bar_1.step()
        off_switchs("sorter")
    print(' Done')
    Sorter_thread = threading.Thread(target=run_sorter)
    Sorter_thread.start()


def Backup_core(src, dst, symlinks=False, ignore=None):
    def run_backup():
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            if backup_switch == False:
                break
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                Backup_core(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    copy2(s, d)
                    print('copying: ', s, 'to: ', d)
    backup_thread = threading.Thread(target=run_backup)
    backup_thread.start()


def Offloder_core():
    def run_Offloder():
        def if_connected():
            # gets path from list
            for path in list_of_paths_to_offlode:
                # checks if the drive is conected
                if os.path.exists(path) == True:
                    # tells the offlode def drive is conected
                    offlode_card(path)
                    # passes the path
                    off_switchs("offlode")
        # move files off sd card

        def offlode_card(sd):
            # walks the directory
            for dirName, subdirList, fileList in os.walk(sd, topdown=False):
                filecount2 = len(dirName) + len(subdirList) + len(fileList)
                progress_bar_3['maximum'] = filecount2
                for fname in fileList:
                    if Offloder_switch == False:
                        break
                    # comdins to path with the file name
                    pathtofile = dirName + "/" + fname
                    pathtopop = sorter_in + "/" + fname
                    if os.path.exists(pathtopop) == False:
                        try:
                            print("Copying: " + fname)
                            move(pathtofile, sorter_in)
                        except:
                            pass
                    else:
                        print(fname + " duplcet")
                    progress_bar_3.step()

        print("scaning")
        if_connected()
        sleep(6)

    Offloder_thread = threading.Thread(target=run_Offloder)
    Offloder_thread.start()


# ##cores.end###
# ## progres bar ###
progress_bar_1 = Progressbar(root, orient=HORIZONTAL,
                             length=270, mode='determinate')
progress_bar_1.grid(row=8, column=0)

progress_bar_2 = Progressbar(root, orient=HORIZONTAL,
                             length=270, mode='determinate')
progress_bar_2.grid(row=11, column=0)

progress_bar_3 = Progressbar(root, orient=HORIZONTAL,
                             length=270, mode='determinate')
progress_bar_3.grid(row=4, column=0)
# ## progres bar.end ###

open_save()
root.mainloop()
