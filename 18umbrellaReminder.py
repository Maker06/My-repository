# Umbrella reminder program
# project picked from chapter 16 of Automate the Boring Stuff with Python

# THINGS YOU MAY WANT TO CHANGE AFTER YOU HAVE THIS PROGRAM:
# line 22: the URL should be the 7-day forecast page for your own location
# line 68: my_number should be the phone number at which you'd like to receive texts

import re

# THE BELOW MODULES DO NOT COME WITH PYTHON; YOU NEED TO INSTALL THEM
# try typing these into the terminal/command line:
# pip install requests
# pip install beautifulsoup4
# pip install twilio
import requests, bs4
from twilio.rest import Client
# Requests: downloads stuff from Internet
# Beautiful Soup: parses HTML
# Twilio: text message capability

# get page; CURRENTLY SET Myrne, Nadvirna, UA
page = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B8%D1%80%D0%BD%D0%B5-303015983")
page.raise_for_status()
page_soup = bs4.BeautifulSoup(page.text, "html.parser")

# look for rain keywords in certain places (e.g. "chance of precipitation")

# it looks like we want the top two rows (daytime/nighttime) of the table under "Detailed Forecast")
# select element with class "p3" inside element with class "weatherDetails" inside element with id "mainContentBlock"
# which shows  the weather at 8 o'clock
# select element with class "p4" inside element with class "weatherDetails" inside element with id "mainContentBlock"
# which shows the weather at 11 o'clock
#forecast_rows = page_soup.select("#mainContentBlock .weatherDetails .p3")
forecast_8 = page_soup.select("#mainContentBlock .weatherDetails .p3")
forecast_11 = page_soup.select("#mainContentBlock .weatherDetails .p5")
# this makes forecastRows a list of HTML stuff, one "row" from the HTML page per Python list item
print(forecast_8)
print(forecast_11)

# we only care about the second row which might contain keyphrase "дощ"
'''forecast_daytime = forecast_rows[0]
forecast_nighttime = forecast_rows[1]
print('daytime: ', forecast_daytime)
print('nighttime: ', forecast_nighttime)'''

forecast_morning8 = forecast_8[1]
forecast_morning11 = forecast_11[1]
'''print(forecast_morning8)
print(forecast_morning11)'''

# keyword: "Chance of precipitation is xx%." only shows if chance if 20% or higher
# keyword: дощ

# look for associated % and record daytime/nighttime %s
rain_morning8 = False
rain_8_chance = 0
rain_morning11 = False
rain_11_chance = 0
keyphrase = "дощ"
match = re.search(keyphrase, str(forecast_morning8))
regex = re.compile(r'\d\d')
if match:
    rain_morning8 = True
    rain_8_chance = regex.search(str(forecast_8[7])).group()
print(rain_8_chance)

match = re.search(keyphrase, str(forecast_morning11))
if match:
    rain_morning11 = True
    rain_11_chance = regex.search(str(forecast_11[7])).group()
print(rain_11_chance)

print(rain_morning8, rain_morning11)
# if chance of rain:
#   • make a string that has an umbrella reminder, approximate time(s) of (potential) rain, and the associated %s
#   • send text to my number

if rain_morning8 or rain_morning11:
    reminder = "Pack an umbrella! Chances of rain: "
    reminder += str(rain_8_chance) + "% during 8 o'clock, "
    reminder += str(rain_11_chance) + "% during 11 o'clock."
    # for the heck of it:
    print(reminder)

'''
    # prepare to send the text
    auth_sid = "AC3fea6e4e7e285b7b5d4b1c5760252da4"
    auth_token = "9e5a96026d653fbfb944a4ccdbb8f3e8"
    twilio_client = Client(auth_sid, auth_token)
    from_number = "+14159496645"
    my_number = "380976038100" # FILL IN YOUR NUMBER including country code (+1 at the start if USA)
    # time to send the text
    twilio_client.messages.create(body=reminder, from_=from_number, to=my_number)'''