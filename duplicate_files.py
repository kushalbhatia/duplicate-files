''' Write a Python program which will find duplicate files on your computer '''


import os
import hashlib
import time


hashed_files_dict = {}
duplicate_files_list = []
# case sensitive match
ignore_directories_list = ['.git', '.svn', '.vscode']
# start timer for program
start_time = time.process_time()

''' Compute and return the hash for a single file '''


# try/except will catch all errors and skip it
def compute_hash(file):
    try:
        binary_file = open(file, 'rb')
        content_file = binary_file.read()
        hash_file = hashlib.sha1(content_file).hexdigest()
        return hash_file
    except:
        return False


''' Verify if path contains a directory that is in the ignore_directory_list '''


# if path contains a directory from ignore list, return False, otherwise return True
def verify_path(path, ignore_directories_list):
    for ignore_directories in ignore_directories_list:
        if ignore_directories in path:
            return False
    return True


''' Get complete path of file, exclude hidden directories, find hash of file path, and return list of unique duplicates in a given path '''


def file_duplicates(path):
    # find complete path
    for root, directories, files in os.walk(path):
        # if any of the directories listed in ignore_directories_list are found in complete_file_path, skip it
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

            # add hashed file paths to dictionary of hashes
            if hashed_file_path not in hashed_files_dict:
                hashed_files_dict[hashed_file_path] = complete_file_path
            else:
                # add duplicate hashed file paths to list of duplicates
                duplicate_files_list.append(complete_file_path)
                # only add matched duplicate files to list of duplicates
                matching_file = hashed_files_dict[hashed_file_path]
                if matching_file in duplicate_files_list:
                    duplicate_files_list.sort()
                    continue
                duplicate_files_list.append(matching_file)
                # add duplicate files to a separate text file
                duplicates = open('duplicate_files.txt', 'w')
                for duplicate_files in duplicate_files_list:
                    duplicates.write(duplicate_files)
                duplicates.close()

    # return unique sorted list of duplicates
    return duplicate_files_list


# end timer for program
print(f'My program took {time.process_time() - start_time} seconds to run\n')
