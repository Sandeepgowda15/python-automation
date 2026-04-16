import shutil
import time

source = "data.txt"
backup = "backup/data.txt"

while True:
    shutil.copy(source, backup)
    print("Backup completed")
    time.sleep(30)
