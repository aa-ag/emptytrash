############------------ IMPORTS ------------############
import os
import shutil


############------------ GLOBAL VARIABLE(S) ------------############
# terminal must have full disk access 
path_to_trash = "/Users/aaronaguerrevere/.Trash"

files_in_trash = os.listdir(path_to_trash)


############------------ FUNCTION(S) ------------############
def buh_bye_trash():
    for file in files_in_trash:
        # all files in trash
        files_in_trash_path = os.path.join(path_to_trash, file)

        # if is file, remove it and let the user know
        try:
            if os.path.isfile(files_in_trash_path):
                os.remove(files_in_trash_path)
                print("File successfully deleted")
            # otherwise, remove whole directory
            elif os.path.isdir(files_in_trash_path):
                shutil.rmtree(files_in_trash_path)
                print("Directory successfully deleted")

        except Exception as e:
            print(e)

    # once done, let the user know
    print("Trash emptied!")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    buh_bye_trash()