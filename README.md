# A simple yet powerful program that searches for unique sorted duplicate hashed files on ur computer

1. Import os and hashlib modules

2. Look out for exceptions, if caught, skip. Then compute and return hash value for given file by opening and reading binary file, then computing SHA-1 hash

3. Create an empty dictionary of hashed files, an empty list of duplicate files, and a ignore list of hidden directories

4. Add a counter to see how many files are running, then get complete path of file by looping through and utilizing the walk function in the os module, then join the root and file

5. Exclude hidden directories by traversing through all of the "files" (can be directories or files) and compare against ignore_list in a case sensitive manner

6. Find out how long function takes to run from start to finish, and add hashed file paths to dictionary of hashed files, and duplicate hashed files to list of duplicate files

7. Only add matched duplicates to list of duplicate files by skipping additional using continue, and sort

8. Return unique list of duplicate files
