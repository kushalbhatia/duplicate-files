''' Write a Python program which will find duplicate files on your computer '''

import os
import hashlib


''' Compute and return the hash for a single file '''


def compute_hash(file):
    while True:
        try:
            fh = open(file, 'rb')
            content_file = fh.read()
            hash_file = hashlib.sha1(content_file).hexdigest()
        except FileNotFoundError:
            continue
    return hash_file


''' Get complete path of file, exclude hidden directories, find hash of file path, and return list of unique duplicates in a given path '''


def file_duplicates(path):
    hashes_dict = {}
    duplicates_list = []
    # case sensitive match
    ignore_list = ['.git', '.svn', '.DS_Store']
    # find complete path
    for root, directories, files in os.walk(path):
        # file can be a file or a directory
        for file in files:
            if file in ignore_list:
                continue

            # add a counter to see how many files are running
            counter = 0
            while True:
                # find hash of complete path
                complete_file_path = os.path.join(root, file)
                hashed_file_path = compute_hash(complete_file_path)
                counter += 1
                print(f'Now printing number {counter}', complete_file_path)

            # add hashed file paths to dictionary of hashes
            if hashed_file_path not in hashes_dict:
                hashes_dict[hashed_file_path] = complete_file_path
            else:
                # add duplicate hashed file paths to list of duplicates
                duplicates_list.append(complete_file_path)
                # only add matched duplicate files to list of duplicates
                matching_file = hashes_dict[hashed_file_path]
                if matching_file in duplicates_list:
                    duplicates_list.sort()
                    continue
                duplicates_list.append(matching_file)

    # return unique sorted list of duplicates
    return duplicates_list


file_duplicates(
    '/Users/kushal/')
