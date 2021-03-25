import os
import shutil
import random

dir_org = "/Users/tomaszburzy/Desktop/organised folder"
import_dir = '/Volumes/WinInstall/here'
temp_dir = '/Volumes/WinInstall'
bin1 = '/Volumes/WinInstall/bin'

'''
i = 0
while i < 50:
     exclude_prefixes = ('.DS_Store')  # exclusion prefixes
     for dirpath, dirnames, filenames in os.walk(temp_dir):
          # exclude all dirs starting with exclude_prefixes
          dirnames[:] = [dirname
                    for dirname in dirnames
                    if not dirname.startswith(exclude_prefixes)]

     
     filepick = dirpath+'/'+random.choice(filenames)  
     if not os.listdir(dirpath):
          sys.exit('Panos directory is empty')
     
     
     
    
     
     #shutil.move(filepick,import_dir)
     #try to fined a why to get the anser without the '[]' !!!
     i += 1


filePath = '/Users/tomaszburzy/Desktop/temp folder/18 - 05 - 2020'
bin1 = '/Users/tomaszburzy/Desktop/poop'
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    shutil.move(filePath,bin1)
else:
    print("Can not delete the file as it doesn't exists")

'''
os.chdir('/Volumes/WinInstall')
for root, dirs, files in os.walk(temp_dir, topdown=False):
   for name in dirs:
     hello = (os.path.join(root, name))
     
random_dir = random.choice(dirs)


loop1 = 0
while loop1 < 1000:
     for root, dirs, files in os.walk(random_dir):
          files = [f for f in files if not f[0] == '.']
     
     #if not files.remove('.DS_Store'):
     #     print(sweet)

     if len(random_dir)==0:
          print('its empty')
          shutil.move(random_dir,bin1)
     try:
          filepick = root+'/'+random.choice(files)
     except IndexError as error:
          break

     
     shutil.move(filepick,import_dir)

     print(root)
     print(filepick)
     loop1 +=1
