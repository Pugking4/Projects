import os
import random
import subprocess

# specify the directory to search
directory = r"E:\Torrent\Priv"

# create a list to store all image and video files in the directory
media_files = []

# iterate through all subdirectories and files within the directory
for root, dirs, files in os.walk(directory):
    # check if each file is an image or video file
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".mp4", ".mkv", ".avi")):
            # use os.path.join to create the full file path
            full_path = os.path.join(root, file)
            media_files.append(full_path)

try:
    while True:
        # select a random file from the list
        random_file = random.choice(media_files)

        # open the file with the default application for its extension
        subprocess.run([random_file], shell=True)
except KeyboardInterrupt:
    # exit the loop if the script is interrupted with Ctrl+C
    pass
