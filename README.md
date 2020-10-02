# A simple yet powerful program that searches for unique, sorted duplicate hashed files on your computer

1. Import os, hashlib, and time modules

2. Create a global dictionary of hashed files, a global dictionary of duplicate files, a global ignore list of case-sensitive hidden directories, and a timer

3. Try to compute and return hash value for given file by opening and reading binary file, then computing SHA-1 hash. If file cannot be opened, return false

4. Verify if path contains a directory that is in the ignore_directory_list (you can add to this list if you want)

5. If a file exists, create a separate duplicate_files.txt file which will store all of the duplicate_files

6. Get the complete path of file by looping through and using the walk function in the os module, then join the root and file

7. Find hash of complete_file_path, and if that hashed_file_path does not exist, skip it

8. If hashed file path is not already in hashed_files_dict, append the complete_file_path (key) and the hashed_file_path (value) to duplicate_files_dict

9. If there are multiple hashed_file_paths (value), assign the complete_file_path (key) to matching_file

10. If the matching file key already exists in duplicate_files_dict, skip it

11. Append matching_file (key) with hashed_file_path (value) to duplicate_files_dict

12. Write to duplicate_files.txt file using the key (complete_file_path) from duplicate_files_dict

13. Create a csv file called 'all_files.csv' and write all of your path files to it and compare against the duplicate files

14. Merge the duplicate_files and hashed_files dictionaries

15. Find out how long program takes to run from start to finish

16. Return unique sorted dictionary (only keys - complete_file_paths) of duplicates
