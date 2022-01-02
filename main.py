import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder
import pandas as pd

from datetime import datetime
from datetime import timedelta

#user enter the date and time
my_string = str(input('Enter date(yyyy-mm-dd hh:mm): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
 
# decrement of time 10 minutes   
n = 10
past_time = my_date - pd.DateOffset (minutes=n)
print (past_time)

#display the date and time that user enter
print(my_date)

#increment of time 10 minutes
n = 10
ahead_time = my_date + timedelta (minutes=n)
print (ahead_time)

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("issDetails.txt", "w")
file.write("There are currently" +
            str(result["number"]) + "astronout on ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

#print the latitude and longitude
g = geocoder.ip("me")
file.write("\nYour current latitude / longitude is: " + str(g.latlng))
file.close()
webbrowser.open("issDetails.txt")

#set the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("maps.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

#the location (lat/lon) of the ISS
while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    #The ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    
    #Output of the latitude and longitude
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))
    
    #Upate the lotitude and longitude
    iss.goto(lat, lon)

    #change location of the iss every 10 mins
    time.sleep(600)
