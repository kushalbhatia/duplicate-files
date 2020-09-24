# A simple yet powerful program that searches for unique sorted duplicate hashed files on your computer

1. Import os, hashlib and timeit modules

2. Create an empty dictionary of hashed files, an empty list of duplicate files, an ignore list of case-sensitive hidden directories, and a timer

3. Compute and return hash value for given file by opening and reading binary file, then computing SHA-1 hash. Look out for all exceptions/errors; if caught, skip

4. Verify if path contains a folder that is in the ignore_directory_list (you can add to this list if you want)

5. Get complete path of file by looping through and utilizing the walk function in the os module, then join the root and file

6. If any of the folders listed in ignore_directories_list are found in complete_file_path, skip it

7. Add hashed file paths to dictionary of hashed files, and duplicate hashed files to list of duplicate files

8. Only add matched duplicates to list of duplicate files by skipping additional using continue, and sort

9. Find out how long program takes to run from start to finish

10. Return unique sorted list of duplicate files by calling file_duplicates() function and providing a relative or absolute path
