import threading
import os
import time
import shutil
sorter_out = '/Volumes/SSD 1T/mellowtest/sorted'
backup_out = '/Volumes/SSD 1T/mellowtest/Backup'


def callmemaby():
    print('yay he called')


def Backup_core():
    # off_switchs("backup")

    Backup_thread = threading.Thread(
        target=run_backup, args=(sorter_out, backup_out))
    Backup_thread.start()


[os.path.join(r, file) for r, d, f in os.walk(sorter_out) for file in f]
hello = ([os.path.join(r, file)
          for r, d, f in os.walk(sorter_out) for file in f])


def Backup_core():
    def run_backup(src, dst, symlinks=False, ignore=None):
        progress_bar_backup["maximum"] = len(
            [os.path.join(r, file) for r, d, f in os.walk(src) for file in f])
        for r, d, f in os.walk(src):
            for file in f:
                Path_to_file = os.path.join(r, file)
                path_to_save_to = Path_to_file.replace(src, dst)
                path_to_make_dirs = r.replace(src, dst)
                if not os.path.exists(path_to_make_dirs):
                    os.makedirs(path_to_make_dirs)
                    shutil.copy2(Path_to_file, path_to_save_to)
                    print("copying: ", Path_to_file, "to: ", path_to_save_to)
                    progress_bar_backup.step()
        off_switchs("backup")
    Backup_thread = threading.Thread(
        target=run_backup, args=(sorter_out, backup_out))
    Backup_thread.start()
