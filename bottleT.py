__author__ = 'anastassias'

# A very simple Bottle Hello World app for you to get started with...
import json
import urllib.request
from bottle import default_app, route, request

@route('/')
def location():
    my_ip = request.remote_addr
    api_key = 'b9a1a4f176b6b08a35f874845332f54eae3ec9708f43baec9e048587194fda63'
    baseurl = 'http://api.ipinfodb.com/v3/ip-city/'
    url = baseurl + "?key=" + api_key + "&ip=" + my_ip + "&format=json"

    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("UTF8"))
    cityName = (data["cityName"][:])

    weatherBaseLink = 'http://api.openweathermap.org/data/2.5/'
    weatherLink = weatherBaseLink + "weather?q=" + cityName + "&mode=xml"
    yourW = "Your Weather lookup"

    return "Your public ip is: " + my_ip + " and you live near the: " + cityName + " and: " +  """<a href=""" +  weatherLink + """ target="_blank">""" + yourW + """</a>"""


application = default_app()