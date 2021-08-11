############------------ IMPORTS ------------############
import os
import shutil
import settings


############------------ GLOBAL VARIABLE(S) ------------############
# terminal must have full disk access 
trash = settings.path_to_trash

files_in_trash = os.listdir(trash)


############------------ FUNCTION(S) ------------############
def buh_bye_trash():
    for file in files_in_trash:
        # all files in trash
        files_in_trash_path = os.path.join(trash, file)

        # if is file, remove it and let the user know
        try:
            if os.path.isfile(files_in_trash_path):
                os.remove(files_in_trash_path)
                print("File successfully deleted")
            # otherwise, remove whole empty directory
            elif os.path.isdir(files_in_trash_path):
                shutil.rmtree(files_in_trash_path)
                print("Directory successfully deleted")

        except Exception as e:
            print(e)

    # once done, let the user know
    print("Trash emptied!")


# ############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    buh_bye_trash()