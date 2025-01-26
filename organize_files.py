# - Topics:
#  - Learn how to automate tasks using Python scripts.
# - Use os and shutil for file manipulation.
# - Project:
# - Write a Python script that automatically organizes files in a folder
# - by extension (e.g., move .txt files to a "TextFiles" folder).

import shutil, os

def file_path():
    """
    Get the file path to the directory containing the files
    and the new directory where they will be moved/copied to.
    """
    old_directory = input(r"File path to directory 'C:\\...': ")
    new_directory = input(r"File path to new directory: ")

    # Create the new directory if it doesn't exist
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)

    # Get the file extension to move/copy
    file_extention = input("File extension '.txt,.pdf' etc:")

    return old_directory,file_extention,new_directory

def organize_folder(old_directory,file_extention,new_directory):
    """
    Move or copy all files with the specified extension to the new directory.
    """
    choices = input("Enter 'm' to move files or 'c' to copy files to new directory: ")

    # Iterate over all files in the old directory
    for filename in os.listdir(old_directory):
        if filename.endswith(file_extention):
            # Copy or move the file to the new directory
            if choices == "c":
                shutil.copy(os.path.join(old_directory,filename),new_directory)
            else:
                shutil.move(os.path.join(old_directory,filename),new_directory)

    return True


if __name__== "__main__":
    old_directory,file_extension,new_directory = file_path()
    organize_folder(old_directory,file_extension,new_directory)
    print("File organization successful.")
