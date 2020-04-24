import requests
import pandas as pd
import geocoder


# get list of all european countries and capitals incl lattitude and longitude
europe = requests.get('https://restcountries.eu/rest/v2/region/europe?fields=name;capital;latlng;alpha2Code;population')
jsonRes = europe.json()
print('Found: ...')

df = pd.DataFrame(columns=['country', 'capital', 'lat', 'long', 'code', 'population'])
for index, item in enumerate(jsonRes):
    df.loc[index] = [item['name'], item['capital'], item['latlng'][0],
                     item['latlng'][1], item['alpha2Code'], item['population']]


# get more precise lattitude and longitude values
for i in range(len(df)):
    locate = df['capital'][i] + ', ' + df['country'][i]
    response = geocoder.osm(locate)  
    if response.json is not None:
        jsonRes = response.json
        df.loc[i, 'lat'] = jsonRes['lat']
        df.loc[i, 'long'] = jsonRes['lng']
        print(locate)

df.to_csv('EU_capitals.csv', index=False)
print(str(len(df)) + ' European capitals where found and saved to EU_capitals.csv')
