# from sync_folders import main, purgelog, clean
# main.sync('/Volumes/SSD_1T/fello', '/Volumes/SSD_1T/toutorals')

from dirsync import sync

sourcedir = '/Volumes/SSD_1T/toutorals'
targetdir = '/Volumes/SSD_1T/fello'
action = sync
sync(sourcedir, targetdir, action, **options)
