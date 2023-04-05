import requests
import json
import random

#element = input('Enter an element: ')
element = 'no2'

def AQI_string(site):
    AQI_list = ['aqi_no2', 'aqi_o3_8hr', 'aqi_pm10', 'aqi_pm2_5', 'aqi_co']
    AQI_dict = {}
    for AQI in AQI_list:
        if site['name'] == 'Civic' and (AQI == 'aqi_no2' or AQI == 'aqi_co'):
            AQI_dict[AQI] = 'Data not available'
        else:
            try:
                if int(site[AQI]) < 34:
                    AQI_dict[AQI] = 'Very Good'
                elif int(site[AQI]) < 67:
                    AQI_dict[AQI] = 'Good'
                elif int(site[AQI]) < 100:
                    AQI_dict[AQI] = 'Fair'
                elif int(site[AQI]) < 150:
                    AQI_dict[AQI] = 'Poor'
                elif int(site[AQI]) < 201:
                    AQI_dict[AQI] = 'Very Poor'
                else:
                    AQI_dict[AQI] = 'Hazardous'
            except:
                AQI_dict[AQI] = 'Data not available'
    return AQI_dict

def exists(site, element):
    if site['name'] == 'Civic' and (element == 'aqi_no2' or element == 'co' or element == 'aqi_co'):
        return 'Data not available'
    else:
        try:
            site[element]
            return site[element]
        except:
            return 'Data not available'

# specify endpoint
url = 'https://www.data.act.gov.au/resource/94a5-zqnn.json'

# specify parameters
params = {}

# make GET request
response = requests.get(url, params=params)

# load response content into a Python dictionary
data = json.loads(response.content)

# dump data into a JSON file
with open('air_qual.json', 'w') as f:
    json.dump(data, f, indent=4)

output = []
for i in range(3):
    site = data[i]
    AQI_dict = AQI_string(site)
    output.append(f"Site: {site['name']}\nCO PM: {exists(site, 'co')}\nCO AQI: {exists(site, 'aqi_co')} ({AQI_dict['aqi_co']})\nNO2 PM: {exists(site, 'no2')}\nNO2 AQI: {exists(site, 'aqi_no2')} ({AQI_dict['aqi_no2']})\nO3 8hr PM: {exists(site, 'o3_8hr')}\nO3 AQI 8hr: {exists(site, 'aqi_o3_8hr')} ({AQI_dict['aqi_o3_8hr']})\nPM10: {exists(site, 'pm10')}\nPM10 AQI: {exists(site, 'aqi_pm10')} ({AQI_dict['aqi_pm10']})\nPM2.5: {exists(site, 'pm2_5')}\nPM2.5 AQI: {exists(site, 'aqi_pm2_5')} ({AQI_dict['aqi_pm2_5']})\n")
    #print(AQI_string(site))

output = output[0] + '\n' + output[1] + '\n' + output[2]

print(output)