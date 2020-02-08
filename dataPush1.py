import json
import csv
import datetime
import requests
post_request_headers = {
"Content-Type": "application/json"
}
csv_path = 'traffic_accidents.csv'
json_path = 'parsed _data.json'
data = {}
es_url = 'http://116.202.87.166:3718'
es_index = 'acci'
with open(csv_path) as csvdata:
    csvReader = csv.DictReader(csvdata)
    for object_id, in csvReader:
        id = int(row['OBJECTID_1'])
        row['OBJECTID_1']=int(row['OBJECTID'])
        row['INCIDENT_ID']=double(row['INCIDENTID'])
        row['OFFENSE_ID']=doubel(row['OFFENSE_ID'])
        row['OFFENSE_CODE']=double(row['OFFENSE_CODE'])
        del row['OFFENSE_CODE_EXTENSION']
        row['TOP_TRAFFIC_ACCIDENT_OFFENSE']=row['TOP_TRAFFIC_ACCIDENT_OFFENSE'].replace(' ','_')
	row['FIRST_OCCURRENCE_DATE']=datetime.strptime(row['FIRST_OCCURRENCE_DATE'],"%m%d%y %H:%M:%S")
        del row['LAST_OCCURRENCE_DATE']
        row['REPORTED_DATE']=datetime.strptime(row['REPORTED_DATE'],"%m%d%y %H:%M:%S")
        row['INCIDENT_ADDRESS']=row['INCIDENT_ADDRESS'].replace(' ','_')
        row['GEO_X']=double(row['GEO_X'])
        row['GEO_Y']=double(row['GEO_Y'])
        row['GEO_LON']=float(row['GEO_LON'])
        row['GEO_LAT']=float(row['GEO_LAT'])
        row['DISTRICT_ID']=int(row['DISTRICT_ID'])
        row['PRECINCT_ID']=int(row['PRECINCT_ID'])
        del row['BICYCLE_IND']
        del row['PEDESTRIAN_IND']
        data[id] = row
        insert_request = requests.post(url="{}/{}/_doc/{}".format(es_url, es_index, row['OBJECTID_1']),
                                       data=json.dumps(data[id]),
                                       headers=post_request_headers).json()
        print(insert_request)
        # print(row)

with open(json_path,'w')as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))


