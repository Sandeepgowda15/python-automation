import requests
import time

url = "https://google.com"

while True:
    try:
        response = requests.get(url)
        print(f"Status: {response.status_code}")
    except:
        print("Website is DOWN")

    time.sleep(10)
