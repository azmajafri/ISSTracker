import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

from datetime import datetime

#user enter the date and time
my_string = str(input('Enter date(yyyy-mm-dd hh:mm): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")

#display the date and time that user enter
print(my_date)

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("issDetails.txt", "w")
file.write("There are currently" +
            str(result["number"]) + "astronout on ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on boeard" + "\n")

g = geocoder.ip("me")
file.write("\nYour current latitude / longitude is: " + str(g.latlng))
file.close()
webbrowser.open("issDetails.txt")

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    iss.goto(lat, lon)

    time.sleep(15)