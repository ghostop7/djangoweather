from django.shortcuts import render
#this is my views.py file
def home (request):
	import json 
	import requests

	api_request= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=83CEC2D7-31CF-4040-ACDF-0AF568B92838")
	try:
		api=json.loads(api_request.content)
	except Exception as e:
		api="Error .j.."

	
	return render (request,'home.html',{'api':api})

def about(request):
    return render(request, 'about.html', {})