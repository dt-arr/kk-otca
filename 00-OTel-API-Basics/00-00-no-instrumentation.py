import requests

def call_slow_api():
    url = "http://httpbin.org/delay/2"
    response = requests.get(url)
    return response.text

def main():
    print("Calling slow API...")
    result = call_slow_api()
    print("Done! Response length:", len(result))

if __name__ == "__main__":
    main()
