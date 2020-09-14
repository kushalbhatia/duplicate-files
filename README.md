# A simple yet powerful program that searches for unique sorted duplicate hashed files on ur computer

1. Import os and hashlib modules

2. Compute and return hash value for given file by opening and reading binary file, then computing SHA-1 hash

3. Create an empty dictionary of hashed files, and an empty list of duplicate files

4. Get complete path of file by looping through and utilizing the walk function in the os module, then join the root and file

5. Exclude hidden directories by adding an empty list of hidden directories, then copying and replacing directories list with list of hidden directories

6. Add hashed file paths to dictionary of hashed files, and duplicate hashed files to list of duplicate files

7. Only add matched duplicates to list of duplicate files using continue, then sort for ordered files

8. Return unique list of duplicate files
