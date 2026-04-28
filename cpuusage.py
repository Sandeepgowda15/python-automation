import subprocess

print("Checking CPU usage...\n")

result = subprocess.run(
    ["top", "-b", "-n", "1"],
    capture_output=True,
    text=True
)

print(result.stdout)
