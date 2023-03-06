# import required modules
import subprocess
import time

# prompt the user for the difficulty and version
dif = input("What difficulty? ")
ver = input("What version? ")

# define a list of processes to run
processes = [
    subprocess.Popen(["python", "Projects\\maimai SQLite\\Playerdata Process\\maiprocess.py"]),
    subprocess.Popen(["python", "Projects\\maimai SQLite\\insert_playerdata.py"]),
    subprocess.Popen(["python", "Projects\\maimai SQLite\\versionlamp_test2.py", dif, ver])
]

# wait for each process to finish before continuing to the next one
for p in processes:
    p.wait() # wait for the process to finish
    time.sleep(10) # wait for 10 seconds before moving to the next process
