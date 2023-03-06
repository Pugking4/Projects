import subprocess
import time

dif = input("What difficulty? ")
ver = input("What version? ")

processes = [
    subprocess.Popen(["python", "Projects\\maimai SQLite\\Playerdata Process\\maiprocess.py"]),
    subprocess.Popen(["python", "Projects\\maimai SQLite\\insert_playerdata.py"]),
    subprocess.Popen(["python", "Projects\\maimai SQLite\\versionlamp.py", dif, ver])
]

# wait for each process to finish before continuing to the next one
for p in processes:
    p.wait()
    time.sleep(10)
