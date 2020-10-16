# A simple yet powerful program that searches for unique duplicate hashed files on your Windows, mac0S or Linux computer

1. Import os, hashlib, argparse and time modules

2. Create a global dictionary of hashed files, a global dictionary of duplicate files, a global ignore list of directories (you can add to this list if you want) and a timer

3. Create a function called compute_hash that computes and returns the hash value for given file by opening and reading the binary file, then computing SHA-1 hash. If file cannot be opened, return false

4. Verify if the path contains a directory that is in the ignore_directory_list

5. Split at path (os.sep) will automatically split the path at \ for Windows and / for macOS and Linux

6. Add the .lower() method to convert all directories of path to lowercase and remove empty items ('') associated with the starting and ending points of a path (\ or /)

7. Create a function called file_duplicates, which takes three parameters: starting_directory_name, duplicate_files_txt, and all_files_csv

8. Create a counter and if a file exists, create a separate text file which will store all of the duplicate_files

9. Get the complete path of file by looping through and using the walk function in the os module, with starting_directory_name as the parameter, then join the root and file

10. Process the counter and process the file size for each file

11. Find the hash of complete_file_path, and if that hashed_file_path does not exist, skip it

12. If hashed file path is not already in hashed_files_dict, append the complete_file_path (key) and the hashed_file_path (value) to duplicate_files_dict

13. If there are multiple hashed_file_paths (value), assign the complete_file_path (key) to matching_file

14. If the matching file key already exists in duplicate_files_dict, skip it

15. Append matching_file (key) with hashed_file_path (value) to duplicate_files_dict

16. Write to a text file that contains duplicate files using the key (complete_file_path) from duplicate_files_dict

17. Create an optional csv file and write all of the files in path to it (hashed files and duplicate files)

18. Merge the duplicate_files and hashed_files dictionaries

19. Return unique dictionary keys (complete_file_paths) of duplicate files

20. Create parsed arguments for four parameters: starting directory, duplicates file, an optional file for all files, and an optional parameter for user created ignored directories

21. If the ignore_directories argument was provided by the user, parse and append those ignored directories to the ignore_directories_list

22. Allow users to add separate ignored directories by ','

23. The file_duplicates function will have a starting directory name, a text file for duplicates, and an optional csv file for all of the files

24. Find out how long the program takes to run from start to finish via processing time, not clock time

25. Run program using sudo to run as super-user,  granting full administrator privileges, then enter computer password

Notes:

*Must be running Python 3.6 or above to run this program

*Can be run on Windows, macOS and Linux

*If running via sudo, must use python3, unless an alias is created using the command: alias sudo='sudo '

*Run program by providing a starting directory (--directory), a written file for duplicates (--out_duplicate_files), an optional written file for all of the files(--out_processed_files), and an optional user created ignored directories parameter (--ignore_directories)

*This has been thoroughly tested on all of the operating systems listed above. The largest file size was on a Windows machine that had a 6GB file inside of its directory, and the total processing run time for the program was five minutes (100,000 files)
