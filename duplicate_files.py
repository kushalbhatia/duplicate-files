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


''' Get complete path of file, find hash of file, and return list of unique duplicates in a given path '''


def file_duplicates(path):
    dict_of_hashes = {}
    list_of_duplicates = []
    # find complete path
    for root, directories, files in os.walk(path):
        for file in files:
            complete_file_path = os.path.join(root, file)
            # find hash of complete path
            hashed_file = compute_hash(complete_file_path)
            # add hashed files to dictionary of hashes
            if hashed_file not in dict_of_hashes:
                dict_of_hashes[hashed_file] = complete_file_path
            else:
                # add duplicate hashed files to list of duplicates
                list_of_duplicates.append(complete_file_path)
                # only add matched duplicate files to list of duplicates
                matching_file = dict_of_hashes[hashed_file]
                list_of_duplicates.append(matching_file)
        # return unique list of duplicates by using set()
        return set(list_of_duplicates)
