import requests

link = "https://www.zdnet.com"
f = requests.get(link)
print(f.text)