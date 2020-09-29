# A simple yet powerful program that searches for unique, sorted duplicate hashed files on your computer

1. Import os, hashlib and time modules

2. Create a global dictionary of hashed files, a global list of duplicate files, a global ignore list of case-sensitive hidden directories, and a timer

3. Try to compute and return hash value for given file by opening and reading binary file, then computing SHA-1 hash. If file cannot be opened, return false

4. Verify if path contains a directory that is in the ignore_directory_list (you can add to this list if you want)

5. If a file exists, create a separate duplicate_files.txt file which will store all of the duplicate_files

6. Get the complete path of file by looping through and using the walk function in the os module, then join the root and file

7. Find hash of complete_file_path, and if that hashed_file_path does not exist, skip it

8. If hashed_file_path is not already in hashed_files_dictionary, make it into a key in the dictionary and keep looping

9. If hashed_file_path is already in hashed_files_dictionary, add duplicate hashed file paths to list of duplicate files

10. Then obtain the complete file path (value) of hashed_files_dictionary by giving it the hashed_file_path (key) and attach to a variable called matching_file

11. If the matching_file already exists in duplicate_files_list, skip it

12. Within the os.walk() for loop (but outside files for loop), convert duplicate_files_list to strings using the join() method with new line

13. Write each of those duplicate_file_string to duplicate_files.txt, then close duplicate_files.txt

14. Find out how long program takes to run from start to finish

15. Return unique sorted list of duplicate files by calling file_duplicates() and providing a relative or absolute path
