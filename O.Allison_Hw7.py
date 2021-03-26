
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:56:50 2021
@author: oshaanallison
"""
import requests
#from datetime import datetime
from bs4 import BeautifulSoup
#importing module
import sys
city2= sys.argv[1]
#finding the longitude and latitude of Athens
coordinates = input("Enter the coordinates for " + city2)
#open a file from folder
output=open('weather.txt', 'w')

#Url for weather information
url = "https://forecast.weather.gov/MapClick.php?lat=39.32920000000007&lon=-82.09978499999994#.YFlMMS2ZOYU"
page_url = requests.get(url)
#retrieves the html in the url
soup = BeautifulSoup(page_url.content, 'html.parser')
output.write("ATHENS")
# Url for weather in philly
url2= "https://forecast.weather.gov/MapClick.php?lat={}&lon={}4#.YFlMMS2ZOYU"
colist=coordinates.split(",")
phillyurl=url2.format(colist[0],colist[1])
page_phillyurl= requests.get(phillyurl)




container=soup.find_all('div',{'class':'tombstone-container'})
for a in container:
   #displays all classes, temp, windspeed, and day
    s=a.find('p',{'class':'period-name'})
    output.write(s.text+'\n')
    #shows a short description of the weather for each day
    d=a.find('p',{'class':'short-desc'})
    
    
    output.write(d.text+'\n')
    #finds the temperature for each day/night of the week
    c=a.find('p',{'class':'temp'})
    output.write(c.text+'\n')
  
    
    output.write('\n\n')




output.write("philly")

#recieves the html in the url
soup= BeautifulSoup(page_phillyurl.content, 'html.parser')
container=soup.find_all('div',{'class':'tombstone-container'})
for a in container:
       #displays all classes, temp, windspeed, and day
    s=a.find('p',{'class':'period-name'})
    output.write(s.text+'\n')
     #shows a short description of the weather for each day
    d=a.find('p',{'class':'short-desc'})
   

    output.write(d.text+'\n')
   #shows a short description of the weather for each day
    c=a.find('p',{'class':'temp'})
    

    output.write(c.text+'\n')

    
    output.write('\n\n')
#39.9526,-75.1652





output.close()
