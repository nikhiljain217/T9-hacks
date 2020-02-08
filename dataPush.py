import json
import csv
import requests
post_request_headers = {
"Content-Type": "application/json"
}
csv_path = 'traffic_accidents.csv'
json_path = 'parsed_data.json'
data = {}
es_url = 'http://116.202.87.166:3718'
es_index = 'acci'
with open(csv_path) as csvdata:
    csvReader = csv.DictReader(csvdata)
    for row in csvReader:
        id = row['OBJECTID_1']
        data[id] = row
        insert_request = requests.post(url="{}/{}/_doc/{}".format(es_url, es_index, row['OBJECTID_1']),
                                       data=json.dumps(data[id]),
                                       headers=post_request_headers).json()
        print(insert_request)
        # print(row)

with open(json_path,'w')as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))
