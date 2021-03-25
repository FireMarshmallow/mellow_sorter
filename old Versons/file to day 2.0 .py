import os
import shutil
import time


user_name = 'tomaszburzy'#input('enter the pc username')
folder_one ='Import folder'
import_dir ='/Users/'+user_name+'/Desktop/Import folder/'
folder_two ='organised folder'
org_dir ='/Users/'+user_name+'/Desktop/organised folder/'
folder_tree ='temp folder'
temp_dir ='/Users/'+user_name+'/Desktop/temp folder/'
desktop_dir ="/Users/"+user_name+"/Desktop/"




#this bit checks the directory for how many itams are in it
#and then sets the loop counter to the same amount
os.chdir(import_dir)
items_in_import_folder = next(os.walk(import_dir))[2]
count_import = len(items_in_import_folder)
print(count_import)
count_import += 1
cant_count = 0
loop1 = 1
    #loop one is resbonsbul for inporting files from import folder
    #checking the date is was made and puting it in a folder this the same
    #date in the temp folder
while loop1 < count_import: 
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for f in filenames:
            os.path.join(dirpath, f)
    
    #this bit here is the bit that checks the date of the file 
    modificationTime = temp_dir + time.strftime('%d - %m - %Y', time.localtime(os.path.getmtime(f)))
    
    #and this one is the one thst makes the folder from the date but first it check if it exists alrady
    if not os.path.exists(modificationTime):
        os.makedirs(modificationTime)

    #this bit moves the file to the folder with the same date   
    if not os.path.exists(f):
        shutil.move(f,modificationTime)
        #this bit praints a bunch of staff
        print('file',f,'was moved to ',modificationTime)
        print(loop1,'of',count_import )
    else:
        cant_count += 1
        print('file alrady exists ',cant_count)#debug
    loop1 += 1
    