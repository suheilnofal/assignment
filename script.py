#GHCND:US1WAKG0038
import json
from csv import DictReader

#load in data from precipitation & from station csv file
f = open('precipitation.json')
data = json.load(f)

with open('stations.csv') as file:
    reader = DictReader(file)
    items = list(reader)

#calculating total yearly precipitation
overal_yearly_precipitaiton = 0
for input in data:
    overal_yearly_precipitaiton += input['value']

#preparing the output file, and making lists with cities, stations, and states
#such that city[i] and states[i] correspond
output = {}
months = ['01','02','03','04','05','06','07','08','09','10','11','12']

city = []
stations = []
states = []
for item in items:
    city.append(item['Location'])
    stations.append(item['Station'])
    states.append(item['State'])


#we will now iterate over every distinct location
for i in list(range(0, len(city))):

    #this gives us the nested dictionary structure 
    output[city[i]] = {}

    city_dict = output[city[i]]
    city_dict['station'] = stations[i]
    city_dict['state'] = states[i]

    #in this step, we filter the data set to include only the specific location
    specific_station = []
    for input in data:
        if input['station'] == stations[i]:
            specific_station.append(input)

    #we will now calculate the monthly precipitation, and add it to the output
    total_monthly_precipitation = []
    for month in months:
        monthly_precipitation = 0
        for input in specific_station:
            if input['date'].startswith('2010-'+month) == True:
                monthly_precipitation += input['value']
        total_monthly_precipitation.append(monthly_precipitation)

    city_dict['total_monthly_precipitation'] = total_monthly_precipitation

    #we will now calculate the year precipitation, and adds it
    total_yearly_precipitation = 0
    for month in total_monthly_precipitation:
        total_yearly_precipitation += month
    
    city_dict['total_yearly_precipitation'] = total_yearly_precipitation

    #this calculates the relative monthly value, and adds it
    relative_mothly_precipitation = []
    for month in total_monthly_precipitation:
        relative_mothly_precipitation.append(month/total_yearly_precipitation)
    
    city_dict['relative_mothly_precipitation'] = relative_mothly_precipitation

    #this calculates the relative yearly value, and adds it
    relative_yearly_precipitaiton = total_yearly_precipitation / overal_yearly_precipitaiton
    city_dict['relative_yearly_precipitation'] = relative_yearly_precipitaiton

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output, file)