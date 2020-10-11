''' Write a Python program which will find duplicate files on your Windows, mac0S or Linux computer '''


import os
import hashlib
import argparse
import time


hashed_files_dict = {}
duplicate_files_dict = {}
# program will ignore any directory which matches the directory in ignore_directories_list
ignore_directories_list = ['.git', '.svn',
                           '.vscode', 'cache', 'library', 'windows']
# start timer for program
start_time = time.process_time()


''' Compute and return the hash for a single file '''


# try/except block will catch all errors and skip it
def compute_hash(file):
    try:
        binary_file = open(file, 'rb')
        read_binary_file = binary_file.read()
        hash_binary_file = hashlib.sha1(read_binary_file).hexdigest()
        return hash_binary_file
    except:
        return False


''' Verify if path contains a directory that is in the ignore_directory_list '''


# if path contains a directory from ignore_directories_list, return False; otherwise return True
def verify_path(path, ignore_directories_list):
    # split at path (os.sep) will automatically split the path at \ for Windows and / for macOS and Linux
    split_path = path.split(os.sep)
    for split in split_path:
        # Add the .lower() method to convert all directories of path to lowercase and remove blank elements ('') from start and end of path
        if (split.lower() in ignore_directories_list) and (split != ''):
            return False
    return True


''' Create optional text file, get complete path of file, exclude hidden directories, find hash of file path, and return dictionary of unique duplicates in a given path '''


def file_duplicates(starting_directory_name, duplicate_files_txt, all_files_csv):
    # start counter
    count = 0
    # try/except block to check if file exists:
    try:
        duplicates_fh = open(duplicate_files_txt, 'w')
    except:
        print(f'Unable to open: {duplicate_files_txt}')
        exit

    for root, directories, files in os.walk(starting_directory_name):
        # if any of the directories listed in ignore_directories_list are found in complete_file_path (returns False), skip it
        if not verify_path(root, ignore_directories_list):
            continue
        # file first scans files in root, then scans files in directories
        for file in files:
            # find complete file path
            complete_file_path = os.path.join(root, file)
            # process counter
            count = count + 1
            print(f'Now processing file number {count}:{complete_file_path}')
            # find hash of complete_file_path
            hashed_file_path = compute_hash(complete_file_path)
            if hashed_file_path == False:
                continue

            # if hashed_file_path is not already in hashed_files_dict, append the complete_file_path (key) and the hashed_file_path (value) to it
            if hashed_file_path not in hashed_files_dict.values():
                hashed_files_dict[complete_file_path] = hashed_file_path
            else:
                # append the complete_file_path (key) and the hashed_file_path (value) to duplicate_files_dict
                duplicate_files_dict[complete_file_path] = hashed_file_path
                # if there are multiple hashed_file_paths (value), assign the complete_file_path (key) to matching_file
                for path, hashed in hashed_files_dict.items():
                    if hashed_file_path == hashed:
                        matching_file = path
                # if the matching_file key already exists in duplicate_files_dict, skip it
                if matching_file in duplicate_files_dict:
                    continue
                # append matching_file (key) with hashed_file_path (value) to duplicate_files_dict
                duplicate_files_dict[matching_file] = hashed_file_path

    # write to a text file that contains duplicate files using the key (complete_file_path) from duplicate_files_dict
    for complete_file_path, hashed_file_path in duplicate_files_dict.items():
        duplicates_fh.write(complete_file_path + '\n')
    duplicates_fh.close()

    # create a csv file and write all of your path files to it (hashed files and duplicate files)
    all_fh = open(all_files_csv, 'w')
    all_fh.write('Filepaths,Hashes\n')
    # merge the duplicate_files and hashed_files dictionaries
    hashed_files_dict.update(duplicate_files_dict)
    for complete_file_path, hashed_file_path in hashed_files_dict.items():
        all_fh.write(complete_file_path + ',' + hashed_file_path + '\n')
        all_fh.flush()
    all_fh.close()

    # return unique dictionary (only keys - complete_file_paths) of duplicates
    return duplicate_files_dict


# parsing user provided arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dir', required=True)
parser.add_argument('--dup_files', required=True)
parser.add_argument('--all_files', nargs='?')
args, unknown = parser.parse_known_args()
starting_directory_name = args.dir
duplicate_files_txt = args.dup_files
all_files_csv = args.all_files

# the file_duplicates function will have a starting directory name, a text file for duplicates, and an optional csv file for all of the files
file_duplicates(starting_directory_name, duplicate_files_txt, all_files_csv)


# end timer for program
print(
    f'\nThis program took {time.process_time() - start_time} seconds to run')
