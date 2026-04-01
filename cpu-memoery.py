import psutil
import time

while True:
    print("CPU Usage:", psutil.cpu_percent(), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    print("-" * 30)
    time.sleep(2)
