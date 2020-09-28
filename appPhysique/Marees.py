import requests
import arrow
from terminaltables import AsciiTable
api_key = '5fa27ba6-f2a2-11ea-b18b-0242ac130002-5fa27c5a-f2a2-11ea-b18b-0242'

print("Bienvenue,veuillez rentrer votre position:")
print("Latitude")
lat = input()
print("Longitude")
lon = input()

#print("Que voulez vous consulter?")
#print("1: Marees  2: Vent")
#ans = input()


print("Date (DD/MM/YYYY): ")
date_0 = input()
date_1 = f"{str(int(date_0[0:2]) + 1)}/{date_0[3:5]}/{date_0[6:10]}"
print(date_1)
start = arrow.now().floor('day')
end = arrow.now().shift(days=1).floor('day')

response = requests.get(
   'https://api.stormglass.io/v2/tide/sea-level/point',
     params={
       'lat': lat,
         'lng': lon,
          'start': start.to('UTC').timestamp,  # Convert to UTC timestamp
          'end': end.to('UTC').timestamp,  # Convert to UTC timestam
     },
    headers={
        'Authorization': '5fa27ba6-f2a2-11ea-b18b-0242ac130002-5fa27c5a-f2a2-11ea-b18b-0242ac130002'
    }
)

json_data = response.json()
print(json_data)

sg0 = json_data['data'][0]['sg']
sg1 = json_data['data'][1]['sg']
sg2 = json_data['data'][2]['sg']
sg3 = json_data['data'][3]['sg']
sg4 = json_data['data'][4]['sg']
sg5 = json_data['data'][5]['sg']
sg6 = json_data['data'][6]['sg']
sg7 = json_data['data'][7]['sg']
sg8 = json_data['data'][8]['sg']
sg9 = json_data['data'][9]['sg']
sg10 = json_data['data'][10]['sg']
sg11 = json_data['data'][11]['sg']
sg12 = json_data['data'][12]['sg']
sg13 = json_data['data'][13]['sg']
sg14 = json_data['data'][14]['sg']
sg15 = json_data['data'][15]['sg']
sg16 = json_data['data'][16]['sg']
sg17 = json_data['data'][17]['sg']
sg18 = json_data['data'][18]['sg']
sg19 = json_data['data'][19]['sg']
sg20 = json_data['data'][20]['sg']
sg21 = json_data['data'][21]['sg']
sg22 = json_data['data'][22]['sg']
sg23 = json_data['data'][23]['sg']
sg24 = json_data['data'][24]['sg']

station = json_data['meta']['station']['name']
dist = json_data['meta']['station']['distance']
data = []
data.append([date_0])
data.append(['00:00',sg0,'12:00',sg12])
data.append(['01:00',sg1,'13:00',sg13])
data.append(['02:00',sg2,'14:00',sg14])
data.append(['03:00',sg3,'15:00',sg15])
data.append(['04:00',sg4,'16:00',sg16])
data.append(['05:00',sg5,'17:00',sg17])
data.append(['06:00',sg6,'18:00',sg18])
data.append(['07:00',sg7,'19:00',sg19])
data.append(['08:00',sg8,'20:00',sg20])
data.append(['09:00',sg9,'21:00',sg21])
data.append(['10:00',sg10,'22:00',sg22])
data.append(['11:00',sg11,'23:00',sg23])
data.append(["Distance",dist])
table = AsciiTable(data, title=station)

print(table.table)






