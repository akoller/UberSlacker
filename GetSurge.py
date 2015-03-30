#!/usr/bin/python
import requests, json
import settings
from GetLatLong import GetLatLong

def GetSurge():
	work_lat_long = GetLatLong(settings.work_address)
	url = "https://api.uber.com/v1/estimates/price"
	parameters = {
		'server_token':settings.uber_token, 
		'start_latitude':work_lat_long['lat'], 
		'start_longitude':work_lat_long['lng'], 
		'end_latitude':work_lat_long['lat'], 
		'end_longitude':work_lat_long['lng']}
	response = requests.get(url, params=parameters)
	data = response.json()
	print(data['prices'][0]['surge_multiplier'])
	return data['prices'][0]['surge_multiplier']


