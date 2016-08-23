"""
TO DO:
- Adding unknown extensions to miscellaneous folder
- Make it possible to organize into an existing folder (Y/N)
- Stop quitting after organizing
- Add file types: CODE, Subtitles
IDEAS:
- DRY (calling the function)
- Maybe add more functionality (eg. clean folder completely)
"""

import os
import shutil

# Defining the file types

# Documents
word_files = [".doc", ".dot", ".docx", ".docm", ".dotx", ".dotm", ".docb"]
excel_files = [".xls", ".xlsm", ".xltx", ".xltm", ".xlsb", ".xla", ".xlam", ".xll", ".xlw", ".xlt", ".xlm", ".xlsx"]
power_point_files = [".ppt", ".pot", ".pps", ".pptx", ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm", ".sldx", ".sldm"]
publisher_files = [".pub"]
pdf_files = [".pdf"]
text_files = [".txt"]

document_list = []
document_list.append(word_files)
document_list.append(power_point_files)
document_list.append(publisher_files)
document_list.append(pdf_files)
document_list.append(text_files)
document_list.append(excel_files)

# Media
images = [".png", ".jpeg", ".jpg"]
gif = [".gif", ".gifv"]
videos = [".webm", ".mp4", ".mkv", ".flv", ".wmv", ".amv", ".m4v"]
audio = [".mp3", ".wav", ".wma", ".m4a"]

media = []
media.append(images)
media.append(gif)
media.append(videos)
media.append(audio)

# Miscellaneous
compressed = [".rar", ".zip"]

misc_list = []
misc_list.append(compressed)

# Main list

main_list = []
main_list.append(document_list)
main_list.append(media)
main_list.append(misc_list)

# Basic interface/information
print("File Organizer\n")
print("Organizes a directory and creates and new directory inside the first one organized in sub-directories\n")
print("Any file type that isn't recognized is put in the miscellaneous folder along with the other miscellaneous files")
print("\nRun the script on directory which contains the directory to be organized\n")

# Sets path = current dir
path = os.getcwd()  # should be the location of the script

# Gets and manages user input
while True:

    # Getting the directory to be organized

    organize_dir = input("Input the directory name: ")

    # Defining new_path for if statement

    new_path = path + "\\" + organize_dir  # this is the dir to be organized

    # Checking if dir exists and can be organized

    if organize_dir.lower() == 'abort' or organize_dir.lower() == 'exit' or organize_dir.lower() == 'quit':
        print("Exited script")
        exit()
    elif os.path.isdir(new_path):
        break
    else:
        print("Path doesn't exist\nPlease input a valid path\n")

os.chdir(new_path)

# Creates the main directory
while True:

    # Gets the name of the main directory

    main_dir = input("\nName of the main directory: ")

    # Gets the path of the main directory

    main_dir_path = new_path + "\\" + main_dir

    # Checking if dir exists

    if os.path.isdir(main_dir_path):
        print("\nDirectory name already exists\n")
    else:
        break

# Creating main directory
os.mkdir(main_dir)


# Checking for files
def check_files(file, passed_list, new_dir):

    for array in passed_list:

        for extension in array:  # for extension in called array

            if file.endswith(extension):
                func_path = main_dir_path + "\\" + new_dir

                if os.path.isdir(func_path):
                    shutil.move(file, func_path)

                else:
                    os.mkdir(func_path)
                    shutil.move(file, func_path)

"""
def clean(file):

    func_path = main_dir_path + "\\" + "Miscellaneous"

    if os.path.isdir(func_path):
        shutil.move(file, func_path)

    else:
        os.mkdir(func_path)
        shutil.move(file, func_path)
"""

# Calling the function on the files
for file in os.listdir(new_path):
    check_files(file, document_list, "Documents")
    check_files(file, media, "Media")
    check_files(file, misc_list, "Miscellaneous")

print("\nYour '{0}' directory has been organized into a new '{1}' directory!\n".format(organize_dir, main_dir))
