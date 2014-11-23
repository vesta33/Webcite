__author__ = 'anastassias'

import json
import urllib.request
import ipgetter
import xml.etree.ElementTree as ET


api_key = 'b9a1a4f176b6b08a35f874845332f54eae3ec9708f43baec9e048587194fda63'
my_ip = ipgetter.myip()
baseurl = 'http://api.ipinfodb.com/v3/ip-city/'
url = baseurl + "?key=" + api_key + "&ip=" + my_ip + "&format=json"

response = urllib.request.urlopen(url)
content = response.read()
data = json.loads(content.decode("UTF8"))
cityName = (data["cityName"][:])
print("Your live near the: " +  cityName)
print("Your weather forecast: ")
weatherBaseLink = 'http://api.openweathermap.org/data/2.5/'
weatherLink = weatherBaseLink + "weather?q=" + cityName + "&mode=xml"
tree = ET.parse(urllib.request.urlopen(weatherLink))

root = tree.getroot()
for child in root:
   print(child.tag, child.attrib)
