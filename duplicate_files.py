''' Write a Python program which will find duplicate files on your computer '''

import os
import hashlib


''' Compute and return the hash for a single file '''


def compute_hash(file):
    # open and read binary file
    fh = open(file, 'rb')
    content_file = fh.read()
    hash_file = hashlib.sha1(content_file).hexdigest()
    return hash_file


''' Get complete path of file, exclude hidden directories, find hash of file path, and return list of unique duplicates in a given path '''


def file_duplicates(path):
    hashes_dict = {}
    duplicates_list = []
    hidden_list = []
    # find complete path
    for root, directories, files in os.walk(path):
        # extract hidden directories and append to empty list of hidden directories
        for directory in directories:
            if not directory.startswith('.'):
                hidden_list.append(directory)
                # replace and copy entire directories list with list of hidden directories to skip and exclude
                directories[:] = hidden_list
        for file in files:
            complete_file_path = os.path.join(root, file)
            # find hash of complete path
            hashed_file_path = compute_hash(complete_file_path)
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
