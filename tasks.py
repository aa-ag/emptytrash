############------------ IMPORTS ------------############
import os
import shutil
import schedule
import time


############------------ GLOBAL VARIABLE(S) ------------############
# terminal must have full disk access 
trash = "/Users/aaronaguerrevere/.Trash"

files_in_trash = os.listdir(trash)


############------------ FUNCTION(S) ------------############
def create_test_files():
    '''
     creates 3 enumerated test files, each
     with some enumerated text in them; then alerts
     the user when successfully finished.
    '''
    for i in range(1, 4, 1):
        test_file = open(f"test_file_number_{i}.txt", 'w')

        test_file.write(f"Testing {i}, testing {i}, testing {i}.")
        test_file.write(f"\nTesting {i}.\ntesting {i}.\ntesting {i}.")

        test_file.close()

        print(f"Test file #{i}/3 successfully created.")


def delete_test_files():
    '''
     reads entire project directory
     and sends test files to trash.
    '''
    # walk/pierce thru project file structure
    for root, directories, files in os.walk("."):
        # check all files
        for filename in files:
            # if it's a text file
            if '.txt' in filename:
                # move it to the trash
                # a delete will be terminal
                # and won't send to trash
                print(f"Sending \"{filename}\" to the trash.")
                shutil.move(filename, trash)


def buh_bye_trash():
    '''
     alerts user of what's in the trash, loops thru 
     all files, deletes each whether it's a file or
     a directory;  let's user know every time, and
     at the end too once everything has been deleted
    '''

    print(f"here's everything that was in your trash: {files_in_trash}")

    for i, file in enumerate(files_in_trash):
        # all files in trash
        files_in_trash_path = os.path.join(trash, file)

        # if is file, remove it and let the user know
        try:
            if os.path.isfile(files_in_trash_path):
                os.remove(files_in_trash_path)
                print(f"file {i+1}/{len(files_in_trash)} successfully deleted")
            
            # otherwise, remove whole empty directory
            elif os.path.isdir(files_in_trash_path):
                shutil.rmtree(files_in_trash_path)
                print(f"file {i+1}/{len(files_in_trash)} (Directory) successfully deleted")

        except Exception as e:
            print(e)

    # once done, let the user know
    print("Trash emptied!")


############------------ DRIVER CODE ------------############
buh_bye_trash()

# if __name__ == "__main__":
#     buh_bye_trash()
    # create_test_files()
    # delete_test_files()

    # sets frequency for test file deletion in seconds
    # schedule.every(7).days.do(buh_bye_trash)

    # # create loop to keep running
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    