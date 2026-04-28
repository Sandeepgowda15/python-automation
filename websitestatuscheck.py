
import requests

url = "https://google.com"

try:
    response = requests.get(url)
    print(f"Status: {response.status_code}")
except:
    print("Website is DOWN")
