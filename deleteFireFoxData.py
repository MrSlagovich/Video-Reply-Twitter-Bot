import shutil
import glob
import os

base_path = r"C:\Users\Bryan Adams\AppData\Local\Temp" # enter the dir name

dir_list = glob.iglob(os.path.join(base_path, "rust_mozprofile*"))
for path in dir_list:
    if os.path.isdir(path):
        shutil.rmtree(path)

