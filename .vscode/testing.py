import os
import shutil
import time

test_file = '/Users/tomaszburzy/Desktop/Mellow_site_assets/IMG_6939.jpg'

this = test_file
modificationTime = time.strftime('%d', time.localtime(os.path.getmtime(this)))
monthname = time.strftime("%B", time.localtime(os.path.getmtime(this)))
monthnom = time.strftime("%m", time.localtime(os.path.getmtime(this)))
month = monthnom + " - " + monthname
modificationTime2 = time.strftime(
    '%Y', time.localtime(os.path.getmtime(this)))

print (modificationTime)
print(month)
print(modificationTime2)