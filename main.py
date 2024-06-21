import os
import shutil
from module import switch_case, default_file_name_and_extension

dir_names = []

try:
    path = input("[+] Please enter the path where you want to organize your files : ")
    os.chdir(path)
    files_and_dirs = os.listdir(path)
    files_and_dirs_name = [os.path.splitext(file) for file in files_and_dirs]
    files_name_with_extension = [file for file in files_and_dirs_name if file[1]!='']
    for i in range(len(files_name_with_extension)):
        folder_name = switch_case(files_name_with_extension[i][1], default_file_name_and_extension)
        if folder_name:
            file_name = files_name_with_extension[i][0]+files_name_with_extension[i][1]
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
            shutil.move(f"{path}/{file_name}", f"{path}/{folder_name}/{file_name}")
            if folder_name not in dir_names:
                dir_names.append(folder_name)

    while True:
        print("[+] Do you want to keep the directory names like that? (yes/no) : ")
        for name in dir_names:
                print(f"--> {name}")
        mode = input().lower()
        print("\n\n")
        if mode == "no" :
            for i in range(len(dir_names)):
                print(f"{i+1} --> {dir_names[i]}")
            num = int(input("[+] Choose the file whose name you want to change : "))
            print("\n")
            new_name = input("[+] Now enter the name you want to use : ")
            os.rename(dir_names[num-1], new_name)
            dir_names[num-1] = new_name
        else: 
            break

    print("\n \t[+] Exiting ..... ")
    print("\n")

except FileNotFoundError:
    print("[-] ERROR! this Directory not found Please Make sure to provide the correct path.")

except Exception:
    print("[-] ERROR! There Something Wrong Please Try again and make sure there no error this time")