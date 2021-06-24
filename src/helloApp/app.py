import requests

def main():
    r = requests.get('https://www.google.com/')
    print(r.text)
