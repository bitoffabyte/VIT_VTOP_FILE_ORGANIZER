import os
import sys
import re
import shutil
check = re.compile(r'SEM20\d\d-\d\d_(\w{3}\d{4}).+-20\d\d_(.+)')
currentDir = os.getcwd()
os.chdir(currentDir)
files = os.listdir()
validFiles = [file for file in files if os.path.isfile(file)]
for i in validFiles:
    m = check.search(i)
    if m:
        folderName = m.group(1)
        name = re.sub(r'-+|_+|\s+',' ',m.group(2))
        if os.path.isdir(folderName):
            shutil.move(i, folderName + '/' + name)
        else:
            os.mkdir(folderName)
            shutil.move(i,folderName + '/' +name)