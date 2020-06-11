import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

payload = {
    'mbrLoginId': 'polojdc',
    'password': '*016727a7'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    login_url = "https://www.netflix.com"
    r = s.get(login_url, headers=headers)
    # print(r.content)

    login_url2 = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110"
    # soup = BeautifulSoup(r.content, 'html5lib')
    # print(soup.title)
    r1 = s.post(login_url2, data=payload)
    # print(r1.content)
    # print(r1.status_code)

    r2 = s.get("https://member.ssg.com/myssg/myinfoMng/shpplocNacctMng.ssg?quick=shpplocNacctMng")

    print(r2.status_code)
    print(r2.content)