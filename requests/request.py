import requests

resp = requests.get('http://www.163.com')

print(resp.status_code)

print(resp.headers['content-type'])

print(resp.encoding)

print(resp.cookies)

print(resp.content)

