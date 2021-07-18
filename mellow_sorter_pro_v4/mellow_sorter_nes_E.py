bimport os
from shutil import move
import time

in_folder = '/Volumes/SSD_1T/untitled folder'
out_folder = '/Volumes/SSD_1T/sorted'


def run_sorter(in_path, out_path):
    for subdir, dirs, files in os.walk(in_path):
        for item in files:
            Path_2_item = os.path.join(subdir, item)
            try:
                day = time.strftime(
                    "%d", time.localtime(os.path.getmtime(Path_2_item))
                )

                monthname = time.strftime(
                    "%B", time.localtime(os.path.getmtime(Path_2_item))
                )

                monthnom = time.strftime(
                    "%m", time.localtime(os.path.getmtime(Path_2_item))
                )
                month = monthnom + " - " + monthname

                year = time.strftime(
                    "%Y", time.localtime(os.path.getmtime(Path_2_item))
                )
            except FileNotFoundError:
                pass

            day_name = day + " - " + monthnom + " - " + year
            pathtochack = os.path.join(out_path, year, month, day_name)

            if not os.path.exists(pathtochack):
                os.makedirs(pathtochack)

            pathtochack2 = os.path.join(pathtochack, item)
            if not os.path.exists(pathtochack2):
                try:
                    move(Path_2_item, pathtochack)
                    print(item, "copyed")
                except:
                    print(item, "exists")
    print("sorting Finisht")


run_sorter(in_folder, out_folder)
