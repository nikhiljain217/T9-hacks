import json
import csv

csv_path = 'traffic_accidents.csv'
json_path = 'parsed_data.json'
data = {}
with open(csv_path) as csvdata:
    csvReader = csv.DictReader(csvdata)
    for row in csvReader:
        id = row['OBJECTID_1']
        data[id] = row
        # print(row)

with open(json_path,'w')as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))
