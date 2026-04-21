import shutil

total, used, _ = shutil.disk_usage("/")
if used / total > 0.8:
    print("Disk almost full!")
