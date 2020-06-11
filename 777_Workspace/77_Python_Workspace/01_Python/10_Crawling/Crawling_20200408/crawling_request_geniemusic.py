import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

param = {
    'uxd' : 'polojdc',
    'uxx' : '*016727a7'
}

url1 = "https://www.genie.co.kr/auth/signIn"


s = requests.Session()
req1 = s.get(url1, headers = header)
# print(req1.status_code)
# print(req1.content)

req2 = s.post(url1, data = param, headers = header)
# print(req2.status_code)
soup1 = BeautifulSoup(req2.content, 'html5lib')

req3 = s.get("https://www.genie.co.kr/myMusic", headers = header)
print(req3.content)
print(req3.status_code)

soup2 = BeautifulSoup(req3.content, 'html5lib')

req4 = s.get("https://www.genie.co.kr", headers = header)
# print(req4.status_code)
# print(req4.content)
# soup2 = BeautifulSoup(req4.content, 'html5lib')

