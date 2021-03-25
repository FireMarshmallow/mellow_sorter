import os 
import random
import shutil

Dar = ('/Users/tomaszburzy/Desktop/org')
i = 1
while i < 10:
    if len(Dar) == 0: 
        print("Empty directory")
        break
    Day_folderpath = random.choice(os.listdir(Dar))

    if Day_folderpath[5:7] == '01':
        directory = '01 - January'
    if Day_folderpath[5:7] == '02':
        directory = '02 - February'
    if Day_folderpath[5:7] == '03':
        directory = '03 - March'
    if Day_folderpath[5:7] == '04':
        directory = '04 - April'
    if Day_folderpath[5:7] == '05':
        directory = '05 - may'
    if Day_folderpath[5:7] == '06':
        directory = '06 - June'
    if Day_folderpath[5:7] == '07':
        directory = '07 - July'
    if Day_folderpath[5:7] == '08':
        directory = '08 - August'
    if Day_folderpath[5:7] == '09':
        directory = '09 - September'
    if Day_folderpath[5:7] == '10':
        directory = '10 - October'
    if Day_folderpath[5:7] == '11':
        directory = '11 - November'
    if Day_folderpath[5:7] == '12':
        directory = '12 - December'
    parent_dir = "/Users/tomaszburzy/Desktop/hello"
    path = os.path.join(parent_dir, directory) 
    try: 
        os.makedirs(path, exist_ok = True) 
        print("Directory '%s' created successfully" %directory) 
    except OSError as error: 
        print("Directory '%s' can not be created") 

    original = '/Users/tomaszburzy/Desktop/org/' + str(Day_folderpath)
    target = "/Users/tomaszburzy/Desktop/hello/" + str(directory)
    shutil.move(original,target)
    i+=1
print('bye')

