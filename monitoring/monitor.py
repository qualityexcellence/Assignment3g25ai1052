import psutil
import time
import os

THRESHOLD = 75

print("Monitoring started...")

while True:
  cpu = psutil.cpu_percent(interval=2)
  ram = psutil.virtual_memory().percent

  print(f"CPU: {cpu}% } RAM: {ram}%")

  if cpu > THRESHOLD or ram > THRESHOLD:
    print("Threshold exceeded - scaling to GCP VM")

    # call your existing GCP script here
    os.system(bash scale_to_cloud.sh")
    break

  time.sleep(5)
