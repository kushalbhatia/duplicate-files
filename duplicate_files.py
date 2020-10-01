''' Write a Python program which will find duplicate files on your computer '''


import os
import hashlib
import time


hashed_files_dict = {}
duplicate_files_dict = {}
# case sensitive match
ignore_directories_list = ['.git', '.svn', '.vscode']
# start timer for program
start_time = time.process_time()


''' Compute and return the hash for a single file '''


# try/except block will catch all errors and skip it
def compute_hash(file):
    try:
        binary_file = open(file, 'rb')
        content_file = binary_file.read()
        hash_file = hashlib.sha1(content_file).hexdigest()
        return hash_file
    except:
        return False


''' Verify if path contains a directory that is in the ignore_directory_list '''


# if path contains a directory from ignore_directories_list, return False; otherwise return True
def verify_path(path, ignore_directories_list):
    for ignore_directories in ignore_directories_list:
        if ignore_directories in path:
            return False
    return True


''' Create optional text file, get complete path of file, exclude hidden directories, find hash of file path, and return list of unique duplicates in a given path '''


def file_duplicates(path):
    # try/except block to check if file exists:
    try:
        filename = 'duplicate_files.txt'
        duplicates_fh = open(filename, 'w')
    except:
        print(f'Unable to open: {filename}')
        exit

    for root, directories, files in os.walk(path):
        # if any of the directories listed in ignore_directories_list are found in complete_file_path (returns False), skip it
        if not verify_path(root, ignore_directories_list):
            continue
        # file first scans files in root, then scans files in directories
        for file in files:
            # find complete file path
            complete_file_path = os.path.join(root, file)
            # find hash of complete file path
            hashed_file_path = compute_hash(complete_file_path)
            if hashed_file_path == False:
                continue

            # if hashed file path is not already in hashed_files_dict, complete_file_path is the key and hashed_file_path is the value in hashed_files_dict
            if hashed_file_path not in hashed_files_dict:
                hashed_files_dict[complete_file_path] = hashed_file_path
            else:
                # add duplicate complete_file_path to dictionary of duplicate files
                duplicate_files_dict[complete_file_path] = hashed_file_path
                #
                matching_file = hashed_files_dict[hashed_file_path]
                # if the matching file already exists in duplicate_files_dict, skip it
                if matching_file in duplicate_files_dict:
                    continue
                # append matching file to duplicate_files_dict
                duplicate_files_dict[matching_file] = hashed_file_path

    # write to duplicate_files.txt file the key (complete_file_path) and the value (hashed_file_path) of the duplicate files
    for complete_file_path, hashed_file_path in duplicate_files_dict.items():
        duplicates_fh.write(complete_file_path)
        duplicates_fh.flush()
        duplicates_fh.write(hashed_file_path)
        duplicates_fh.flush()
    duplicates_fh.close()

    # create a csv file called 'all_files.csv' and write all of your path files to it and compare against the duplicate files
    all_fh = open('all_files.csv', 'w')
    all_fh.write('Filepaths,Hashes\n')
    for complete_file_path, hashed_file_path in hashed_files_dict.items():
        all_fh.flush()
        all_fh.write(complete_file_path + ',' + hashed_file_path + '\n')
        all_fh.flush()
        # merge the duplicate_files and hashed_files dictionaries
        duplicate_files_dict.update(hashed_files_dict)
    all_fh.close()

    # return unique sorted dictionary of duplicates
    return sorted(duplicate_files_dict)


# end timer for program
print(
    f'My program took {time.process_time() - start_time} seconds to run\n')


# call the file duplicates() function and give it an absolute or relative path as the parameter
file_duplicates('')
