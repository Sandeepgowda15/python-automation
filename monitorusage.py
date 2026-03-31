import shutil
import time

while True:
    total, used, free = shutil.disk_usage("/")
    
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
    print("-" * 30)
    
    time.sleep(5)
