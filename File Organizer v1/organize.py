"""
Separate videos from images
Prohibit prohibited signs for directory name
Duplicates :(
"""

import os
import shutil

# DEFINING FILE TYPES

# Documents

documents = [".doc", ".dot", ".docx", ".docm", ".dotx", ".dotm", ".docb", ".xls", ".xlsm", ".xltx", ".xltm",
                 ".xlsb", ".xla", ".xlam", ".xll", ".xlw", ".xlt", ".xlm", ".xlsx", ".ppt", ".pot", ".pps", ".pptx",
                 ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm", ".sldx", ".sldm", ".pub", ".pdf", ".txt"]

# Media

media = [".png", ".jpeg", ".jpg", ".gif", ".gifv", ".webm", ".mp4", ".mkv", ".flv", ".wmv", ".amv", ".m4v", ".mp3",
         ".wav", ".wma", ".m4a", ".aqt", ".gsub", ".jss", ".sub", ".ttxt", ".pjs", ".psb", ".rt", ".smi", ".stl",
         ".ssf", ".srt", ".ssa", ".ass", ".usf"]


# Miscellaneous
miscellaneous = [".rar", ".zip"]


# INPUT AND USER INTERACTION
print("File Organizer\n")
print("Organizes a directory and creates a new directory inside the first one organized in sub-directories")
print("Any file type that isn't recognized is put in the miscellaneous folder along with the other miscellaneous files")
print("Any file in the target directory with the same name of a file in the new directory will be ignored")
print("Run the script in the desired directory or in the directory containing the directory to be organized\n")

# Sets path = current dir
path = os.getcwd()  # should be the location of the script

# Gets the directory to be organized
while True:

    organize_dir = input("Input the name of the directory you wish to organizer or leave it blank if you're in it: ")

    # Defining new_path for if statement

    new_path = path + "\\" + organize_dir  # this is the dir to be organized

    # Checking if dir exists and can be organized

    if organize_dir.lower() == 'abort' or organize_dir.lower() == 'exit' or organize_dir.lower() == 'quit':
        print("Exited script")
        exit()
    elif os.path.isdir(new_path):
        break
    else:
        print("\nPath doesn't exist. Please input a valid path\n")

os.chdir(new_path)

# Gets the name of the main directory
while True:

    main_dir = input("\nName of the main directory: ")

    # Gets the path of the main directory

    main_dir_path = new_path + "\\" + main_dir

    # Checking if dir exists
    if main_dir:
        if os.path.isdir(main_dir_path):
            print("\nDirectory name already exists")
        else:
            os.mkdir(main_dir)
            break
    else:
        print("\nPlease input a valid answer")


# FUNCTIONS FOR FILE MANAGEMENT
def check_files(file, passed_list, new_dir):

        for extension in passed_list:

            if file.endswith(extension):
                func_path = main_dir_path + "\\" + new_dir

                if os.path.isdir(func_path):
                    shutil.move(file, func_path)

                else:
                    os.mkdir(func_path)
                    shutil.move(file, func_path)


def clean(file):

    func_path = main_dir_path + "\\" + "Miscellaneous"

    if not file.endswith(main_dir) and not file.endswith(os.path.basename(__file__)):

        if os.path.isdir(func_path):
            shutil.move(file, func_path)

        else:
            os.mkdir(func_path)
            shutil.move(file, func_path)

    else:
        pass

for file in os.listdir(new_path):
    check_files(file, documents, "Documents")
    check_files(file, media, "Media")
    check_files(file, miscellaneous, "Miscellaneous")

for file in os.listdir(new_path):
    clean(file)

# FINAL INFORMATION

if organize_dir:
    print("\nYour '{0}' directory has been organized into the '{1}' directory!".format(organize_dir, main_dir))
else:
    print("\nThis directory has been organized into the '{0}' directory".format(main_dir))