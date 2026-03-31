import subprocess
import os
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(result.stdout)
