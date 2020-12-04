import os
import shutil

# terminal must have full disk access 
path_to_trash = "/Users/aaronaguerrevere/.Trash"

files_in_trash = os.listdir(path_to_trash)

for file in files_in_trash:
    files_in_trash_path = os.path.join(path_to_trash, file)
    try:
        if os.path.isfile(files_in_trash_path):
            os.remove(files_in_trash_path)
            print("File successfully deleted")
        elif os.path.isdir(files_in_trash_path):
            shutil.rmtree(files_in_trash_path)
            print("Directory successfully deleted")
    except Exception as e:
        print(e)

print("Trash emptied!")