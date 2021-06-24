import requests

def main():
    r = requests.get('https://www.google.com/')
    print("Google said "+ str(r.status_code))

if __name__=='__main__':
    main()
