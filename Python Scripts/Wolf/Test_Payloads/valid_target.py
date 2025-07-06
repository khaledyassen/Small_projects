import requests

if __name__ == '__main__':
    try:
        # url_ = input("Enter a target Path: ")
        with open('/home/hackerman/Wolf/Test/targets.txt', 'r') as f:
            for url in f:
                try:
                    response = requests.get(url.strip(), proxies=None)
                    print(response.status_code)
                    # Add further processing here if needed
                except requests.RequestException as req_err:
                    print(f"Error for URL '{url.strip()}': {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
