import subprocess
import time

# Path to the script you want to restart
script_path = "auto.py"

while True:
    print("Starting the script...")
    process = subprocess.Popen(["python", script_path])
    time.sleep(600)  # Wait for 10 minutes (600 seconds)
    print("Stopping the script...")
    process.terminate()
    process.wait()
