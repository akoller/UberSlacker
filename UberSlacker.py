#!/usr/bin/python
import requests, json
import settings
from GetSurge import GetSurge

surge = GetSurge()
url = settings.slack_url
parameters = {
	'token' : settings.slack_token,
	'channel' : settings.slack_channel
}
message = "Uber surge pricing is now " + str(surge) + "x"
response = requests.post(url, params = parameters, data = message)
# data = response.json()
print(response.status_code)
print(response.text)
print(response)