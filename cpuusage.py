import os
import time

while True:
    os.system("top -b -n1 | head -5")
    time.sleep(5)
