# This script is extract information from files in the working directory.
# This script will also store the list of dictionaries.

import os

def find_file_info(directory):
    """"
    To obtainn the name and size of files in designated directory.
    This function takes a directory path as an input and returns the list of directories.
    The List will contain the file's name and size.

    Args:
        dir_path(str): The path to the directory to scan
    
    Returns:
        list: Each of list of dictionary will have the name and size.
    """

    list_of_files = [] #An email list to store the information for the files

    try:
        files_in_cwd = os.listdir(directory)
    except OSError as ERROR:
        print(f"Cannot locate file: {directory} - {ERROR}")
        return []
    
    for file in files_in_cwd:
        full_file_path = os.path.join(directory, file)

        if os.path.isfile(full_file_path):
            try:
                filesize = os.stat(full_file_path).st_size
                fileinfo= {
                    "name": file,
                    "size": filesize 
                }
                list_of_files.append(fileinfo)
            except OSError as ERROR:
                print (f"Can not locate size of the file: {full_file_path} - {ERROR}")

    return list_of_files

#Main Function of the script to call the file information (name and size) and print the output.
def main():

    main_directory = os.getcwd()
    print(f"Scanning directory, Please wait: {main_directory}")

    #Locate Name and Size of the file
    file_data_list = find_file_info(main_directory)

    if file_data_list:
        print("Files and sizes:")
        for file_data in file_data_list:
            print (f"  {file_data['name']}: {file_data['size']} bytes")
    else:
        print("No file of that name exists")
    print('Finished') 
    
if __name__ == "__main__":
    main()
