import os
import shutil
import time
import threading
from shutil import copy2

sou = '/Volumes/SSD 1T/mellowtest/sorted'
buckup = '/Volumes/SSD 1T/mellowtest/Backup'


def runbackup():
    def Backup_core(src, dst, symlinks=False, ignore=None):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                Backup_core(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    copy2(s, d)
                    print('copying: ', s, 'to: ', d)
    backup_thread = threading.Thread(target=Backup_core(sou, buckup))
    backup_thread.start()


runbackup()
