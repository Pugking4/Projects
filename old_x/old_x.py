# import required modules
import os
import shutil

# define a list of file extensions to match
ext = ['.png','.jpg','.jpeg','.gif','.webp']

# initialize counters and lists
count = 0
match_file = []

# define the directory to search for files
directory = "E:\Private"

# get a list of all files in the directory
files = os.listdir(directory)

# loop through each file in the directory
for file in files:
    # split the filename and extension
    filename, extension = os.path.splitext(file)
    
    # check if the extension matches the ones we want
    if extension in ext:
        # if it does, add the file to the list of matching files
        match_file.append(file)
    
    # check if the filename contains the string 'old'
    if 'old' in filename:
        # if it does, increment the counter
        count += 1

# create a new directory with the format 'old {count}'
new_directory = f"E:\Private\old {count}"
os.makedirs(new_directory)

# move all matching files to the new directory
for source in match_file:
    # construct the full file path
    fp = f"{directory}\\{source}"
    
    # check if the file exists
    if os.path.exists(fp):
        # if it does, move it to the new directory
        shutil.move(fp, new_directory)
