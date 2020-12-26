import os
import random
import shutil
import time

##### wellcome to mellow photo orgniser #####
# this is my first larg scrips. so, sorry for all the mistakes

print('hello and wellcom')
user_name = input('enter the pc username')
print('im now going to make same folders on your desk top')

folder_one = 'Import folder'
import_dir = '/Users/'+user_name+'/Desktop/Import folder/'
folder_two = 'organised folder'
org_dir = '/Users/'+user_name+'/Desktop/organised folder/'
folder_tree = 'temp folder'
temp_dir = '/Users/'+user_name+'/Desktop/temp folder/'
desktop_dir = "/Users/"+user_name+"/Desktop/"

path = os.path.join(desktop_dir, folder_one)  # makes the import folder works
try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % folder_one)
except OSError as error:
    print("Directory '%s' can not be created")

path = os.path.join(desktop_dir, folder_two)  # makes the orgnise folder works
try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % folder_two)
except OSError as error:
    print("Directory '%s' can not be created")

path = os.path.join(desktop_dir, folder_tree)  # makes the temp folder works
try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % folder_tree)
except OSError as error:
    print("Directory '%s' can not be created")

print('''put photos in the import folder    
when your dane came back here and  
type in 'go' ''')

loop1 = 1

while loop1 < 6:  # user input with loop
    beging = input('type go to conitun: ')
    if beging == 'go':
        break
    else:
        print('unexpected input')
    loop1 += 1

time.sleep(5)

# this looks at the number of item in the import folder and sets the loop cicels
items_in_import_folder = next(os.walk(import_dir))[2]
count_import = len(items_in_import_folder)

loop2 = 0
while loop2 < (count_import):  # this loop puts the items in a folder with the date
    if (count_import) == 0:
        print(' import folder is empty')
    else:
        media_path = random.choice(os.listdir(import_dir))
    os.chdir(import_dir)
    created = os.stat(media_path).st_ctime
    modificationTime = time.strftime(
        '%d - %m - %Y', time.localtime(os.path.getmtime(media_path)))
    os.chdir(temp_dir)
    if not os.path.exists(modificationTime):
        os.makedirs(modificationTime)
    original = import_dir + str(media_path)
    target = temp_dir + str(modificationTime)
    shutil.move(original, target)
    loop2 += 1


noOfDir = 0
# this looks at the numbe of folders in the temp folder and sets the loop cicels
for base, dirs, files in os.walk(temp_dir):
    for directories in dirs:
        noOfDir += 1
loop3 = 0
while loop3 < (noOfDir):  # this loop takes the date folders and puts them in the months folders
    Day_folderpath = random.choice(os.listdir(temp_dir))
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
    path = os.path.join(org_dir, directory)  # tihs make the month folders
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created")

    original = temp_dir + str(Day_folderpath)
    target = org_dir + str(directory)
    try:
        shutil.move(original, target)
    except shutil.Error:  # add some sort of a check for this fix
        print('the folder alredy exists')

    loop3 += 1

print('Good bye')
