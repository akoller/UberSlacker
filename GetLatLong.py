#!/usr/bin/python
import requests, json
import settings
import pprint

def GetLatLong(address):

	url = "http://maps.googleapis.com/maps/api/geocode/json"
	parameters = {
		'address': address
		}
	response = requests.get(url, params=parameters)
	data = response.json()
	return data['results'][0]['geometry']['location']