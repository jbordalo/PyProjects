import os
import shutil

# DEFINING FILE TYPES

# Documents
documents = [".doc", ".dot", ".docx", ".docm", ".dotx", ".dotm", ".docb", ".xls", ".xlsm", ".xltx", ".xltm",
            ".xlsb", ".xla", ".xlam", ".xll", ".xlw", ".xlt", ".xlm", ".xlsx", ".ppt", ".pot", ".pps", ".pptx",
            ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm", ".sldx", ".sldm", ".pub", ".pdf", ".txt", ".py",
            ".js", ".jar", ".cpp"]

# Media
images = [".png", ".jpeg", ".jpg", ".gif", ".gifv"]

videos = [".webm", ".mp4", ".mkv", ".flv", ".wmv", ".amv", ".m4v", ".aqt", ".gsub", ".jss", ".sub", ".ttxt", ".pjs",
          ".psb", ".rt", ".smi", ".stl", ".ssf", ".srt", ".ssa", ".ass", ".usf", ".avi", ".mov", ".mpg"]

audio = [".mp3", ".wav", ".wma", ".m4a", ".aif", ".iff", ".mpa"]

# Miscellaneous
miscellaneous = [".rar", ".zip", ".exe"]


# INPUT AND USER INTERACTION
print("\nFile Organizer\n")
print("Organizes a directory into a new directory organized in categories.")
print("Any file type that isn't recognized is put in the 'Miscellaneous' directory.")
print("Any file in the original directory with the same name of a file in the new directory will be ignored.")
print("Run the script in the desired directory or in the directory containing the one to be organized.\n")

# Sets path = current dir
path = os.getcwd()  # should be the location of the script

# Gets the directory to be organized
while True:

    # Source directory name
    src_dir = input("Input the name of the directory you wish to organizer or leave it blank if you're in it: ")

    # Not prohibiting signs cause the name is filtered in os.path.isdir()

    # Defining src_path for if statement

    src_path = os.path.join(path, src_dir)  # this is the dir to be organized

    # Checking if dir exists and can be organized

    if os.path.isdir(src_path):
        break
    else:
        print("\nPath doesn't exist. Please input a valid path\n")

os.chdir(src_path)

# Gets the name of the main directory
while True:

    while True:

        dst_dir = input("\nName of the destination directory: ")

        # Gets the path of the main directory

        # Prohibited characters for directory name
        no_chars = ["\\", "/", "*", "|", "\"", "<", ">", ":", "?"]


        # Prohibit function to check prohibited signs on a string
        def prohibit(string):
            splat = string.split()
            for wrd in splat:
                y = list(wrd)
                for letter in y:
                    for char in no_chars:
                        if letter == char:
                            return True

        # If there's a prohibited sign print the signs and go back to the naming
        if prohibit(dst_dir):
            print("\nYou've given an invalid sign (\\, /, *, ?, <, >, \", |")
        else:
            break

    # creating the destination directory path
    dst_dir_path = os.path.join(src_path, dst_dir)

    # Checking if dir exists
    if dst_dir:
        if os.path.isdir(dst_dir_path):
            into_existing = input("\nDo you wish to organize into an already existing folder?(Y/N): ").lower()
            if into_existing == 'y':
                break
            else:
                pass
        else:
            os.mkdir(dst_dir)
            break
    else:
        print("\nPlease input a valid answer")

# FUNCTIONS FOR FILE MANAGEMENT


# Checks for duplicate files
def duplicate(file, dst):
    if os.path.exists(os.path.join(dst, file)):
        return True
    else:
        return False


# Checks each file and moves it to dst dir if created. else creates it and then moves
def organize_files(file, passed_list, new_dir, sub_new_dir=''):

        func_path = os.path.join(dst_dir_path, new_dir, sub_new_dir)

        for extension in passed_list:

            if file.endswith(extension):
                if not file.endswith(os.path.basename(__file__)):
                    if os.path.isdir(func_path):
                        if duplicate(file, func_path) == False:
                            shutil.move(file, func_path)
                        else:
                            print("\n" + os.path.basename(file) + " was marked as a duplicate and ignored.")
                    else:
                        os.makedirs(func_path)
                        shutil.move(file, func_path)


# Finds any missing file with an unknown extension and moves it to the miscellaneous directory
def clean(file):

    misc_path = os.path.join(dst_dir_path, "Miscellaneous")

    docs = os.path.join(dst_dir_path, "Documents")
    audio = os.path.join(dst_dir_path, "Media", "Audio")
    videos = os.path.join(dst_dir_path, "Media", "Videos")
    images = os.path.join(dst_dir_path, "Media", "Images")

    if not file.endswith(dst_dir) and not file.endswith(os.path.basename(__file__)):
        if not duplicate(file, docs) and not duplicate(file, audio) and not duplicate(file, videos) \
                and not duplicate(file, images):
            if not duplicate(file, misc_path):
                if os.path.isdir(misc_path):
                    shutil.move(file, misc_path)
                else:
                    os.makedirs(misc_path)
                    shutil.move(file, misc_path)
    else:
        pass

for file in os.listdir(src_path):
    organize_files(file, documents, "Documents")
    organize_files(file, images, "Media", "Images")
    organize_files(file, videos, "Media", "Videos")
    organize_files(file, audio, "Media", "Audio")
    organize_files(file, miscellaneous, "Miscellaneous")


for file in os.listdir(src_path):
    clean(file)


# FINAL INFORMATION

if src_dir:
    print("\nYour '{0}' directory has been organized into the '{1}' directory!\n".format(src_dir, dst_dir))
else:
    print("\nThis directory has been organized into the '{0}' directory!\n".format(dst_dir))
