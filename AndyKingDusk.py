import shutil
import glob
import os
import re
mod_name = "Andy King"
mods_path = r"F:\Program Files (x86)\Steam\steamapps\common\Dusk\SDK\mnt\local\{}".format(mod_name)



myfile = r"F:\Picstures\andymeme.png"


for subdir, dirs, files in os.walk(mods_path):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        
        if filepath.endswith(".png"):
            shutil.copy(myfile,filepath)




            print (file)

