import requests

url = "https://google.com"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Website is UP ✅")
    else:
        print("Website is DOWN ❌")
except:
    print("Error connecting ❌")
