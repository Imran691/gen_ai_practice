# To check status of our request in console
# "python test_body.py"

import requests

r = requests.post('http://127.0.0.1:8000/hi', json={"who":"MOM", "name": "absc"})
# print(r.status_code)
# print(r.headers)
# print(r.json())
print(r.text)   