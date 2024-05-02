import os
import shutil


def create_subfolder_if_not_exists(folder_path, sub_folder_name):
    subfolder_path = os.path.join(folder_path,sub_folder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def clean_dir(folder_path):
   for filename in os.listdir(folder_path):
       if os.path.isfile(os.path.join(folder_path,filename)):
           # print(os.path.join(folder_path,filename))
           fileextension = filename.split('.')[-1].lower()
           sub_folder_name =f"{fileextension.upper()} Files"
           sub_folder_path = create_subfolder_if_not_exists(folder_path,sub_folder_name)
           file_path = os.path.join(folder_path,filename)
           shutil.move(file_path,sub_folder_path)
           print(f"Move {filename} to {sub_folder_name}")



def get_files_from_dir(folder_path):
    if os.path.isdir(folder_path):
        clean_dir(folder_path)
        print("Cleaning complete")
    else:
        print("Enter valid path")


def main():
    folder_path =r'C:\Users\ABHINAV\Dropbox\PC\Downloads'
    print(f"The file path to the download is \n {folder_path}")
    get_files_from_dir(folder_path)


if __name__ == "__main__" :
    main()