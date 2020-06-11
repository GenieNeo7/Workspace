#this is not purely my code! Thanks to Ori for the code
import urllib
import requests

username = 'aceneo777@naver.com'
password = '*016727a7'
params = {
    'email' : username,
    'password' : password
}

s = requests.session()
req = s.get("https://signup.netflix.com/Login")
print(req.status_code)
req1 = s.post("https://signup.netflix.com/Login", params)
print(req1.status_code)
req2 = s.get("https://www.netflix.com/signup")

print(req2.text)
print(req2.status_code)
# params = urllib.urlencode(
# {'email': username,
# 'password': password })
# f = urllib.urlopen("https://signup.netflix.com/Login", params)
# if "The login information you entered does not match an account in our records.       Remember, your email address is not case-sensitive, but passwords are." in f.read():
#     success = False
#     print("Either your username or password was incorrect.")
# else:
#     success = True
#     print("You are now logged into netflix as")