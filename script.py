#GHCND:US1WAKG0038
import json
from csv import DictReader 

#load in data
f = open('precipitation.json')
data = json.load(f)

#code seattle
code = "GHCND:US1WAKG0038"

months = ['01','02','03','04','05','06','07','08','09','10','11','12']

#filter list to only include seattle
only_seattle = []
for item in data:
    if item['station'] == code:
        only_seattle.append(item)

#this list will include the monthly_precipitation
total_monthly_precipitation = []

#we will now add the monthly precipitation:
for month in months:
    monthly_precipitation = 0
    for input in only_seattle:
        if input['date'].startswith('2010-'+month) == True:
                monthly_precipitation += input['value']
    total_monthly_precipitation.append(monthly_precipitation)

#calculating the yearly precipitation using the list of monthly precipitation:
total_yearly_precipitation = 0
for month in total_monthly_precipitation:
    total_yearly_precipitation += month

#calculating the relative monthly precipitation:
relative_mothly_precipitation = []
for month in total_monthly_precipitation:
    relative_mothly_precipitation.append(month/total_yearly_precipitation) 

#this creates a json file with the output as specified below
output = {
     "Seattle": {
          "station": code,
          "state": "WA",
          "total_monthly_precipitation": total_monthly_precipitation,
          "total_yearly_precipitation": total_yearly_precipitation,
          "relative_monthly_precipitation": relative_mothly_precipitation
     }
}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output, file)