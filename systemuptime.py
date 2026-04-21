import psutil, time

boot = psutil.boot_time()
print("Uptime:", time.time() - boot)
