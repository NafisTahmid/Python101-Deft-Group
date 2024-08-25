import requests
# Making a get request
response = requests.get("https://api.github.com/")
# Print request object
# print(response.url)
# Print status code
# print(response.status_code)
# Print encoding
# print(response.encoding)
# print(response.elapsed)
# print(response.cookies)
# print(response.history)
# print(response.is_permanent_redirect)
# print(response.json())
# print(response.text)
# print(response.status_code)

# Authentication
from requests.auth import HTTPBasicAuth
# Making a get request
# response = requests.get('https://api.github.com/user, ', auth = HTTPBasicAuth('nafisT', 'xxxx'))
# print(response)

# Access an website with an invalid SSL
response = requests.get('https://github.com', verify='/path/to/certfile')
# Print request object
print(response)

# session objects
s = requests.Session()

# Make a get request
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

# Again make a get request
r = s.get('https://httpbin.org/cookies')
# Check if cookie is all set
print(r.text)