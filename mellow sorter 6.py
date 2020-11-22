import os, shutil, time
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected1 = filedialog.askdirectory()
folder_selected2 = filedialog.askdirectory()
path = folder_selected1
for subdir, dirs, files in os.walk(path):
    path = folder_selected1
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    for file in files:
        try:
            this = os.path.join(subdir, file)
            modificationTime =time.strftime('%d', time.localtime(os.path.getmtime(this)))
            modificationTime1 =time.strftime('%m', time.localtime(os.path.getmtime(this)))
            modificationTime2 =time.strftime('%Y', time.localtime(os.path.getmtime(this)))
        except:
            print('Cant find date')
        os.chdir(folder_selected2)
        dayFolder = modificationTime+' - '+modificationTime1+' - '+modificationTime2
        if not os.path.exists(modificationTime2):
            os.makedirs(modificationTime2)
        os.chdir(folder_selected2+'/'+modificationTime2)
        months_nom = ['thisisnothint','01 - January','02 - February','03 - March','04 - April','05 - may','06 - June','07 - July','08 - August','09 - September','10 - October','11 - November','12 - December']
        if not os.path.exists(months_nom[int(modificationTime1)]):
            os.makedirs((months_nom[int(modificationTime1)]))
        os.chdir(folder_selected2+'/'+modificationTime2+'/'+months_nom[int(modificationTime1)])
        if not os.path.exists(dayFolder):
            os.makedirs(dayFolder)
        if not os.path.exists(file):
            try:
                shutil.move(this,dayFolder)
                print(file,'moved')
            except:
                print('cant move',file)
        else:
            print(file,'exists')
print('All done bye')