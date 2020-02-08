import json
import csv
from datetime import datetime
import requests
post_request_headers = {
"Content-Type": "application/json"
}
csv_path = 'traffic_accidents.csv'
json_path = 'parsed _data.json'
data = {}
#es_url = 'http://116.202.87.166:3718'
#es_index = 'acci'
with open(csv_path) as csvdata:
    csvReader = csv.DictReader(csvdata)
    for row in csvReader:
        id = int(row['OBJECTID_1'])
        row['OBJECTID_1']=int(row['OBJECTID_1'])
        row['INCIDENT_ID']=int(float(row['INCIDENT_ID']))
        row['OFFENSE_ID']=int(row['OFFENSE_ID'])
        row['OFFENSE_CODE']=int(row['OFFENSE_CODE'])
        del row['OFFENSE_CODE_EXTENSION']
        #row['TOP_TRAFFIC_ACCIDENT_OFFENSE']=row['TOP_TRAFFIC_ACCIDENT_OFFENSE'].replace(' ','_')
        
        del row['LAST_OCCURRENCE_DATE']
        try:
            #row['FIRST_OCCURRENCE_DATE']=datetime.strptime(row['FIRST_OCCURRENCE_DATE'],"%Y-%m-%d %H:%M:%S")
            #row['REPORTED_DATE']=datetime.strptime(row['REPORTED_DATE'],"%Y-%m-%d %H:%M:%S")
            row['GEO_X']=int(row['GEO_X'])
            row['GEO_Y']=int(row['GEO_Y'])
        except ValueError:
            continue
        row['INCIDENT_ADDRESS']=row['INCIDENT_ADDRESS'].replace(' ','_')
        
        
        row['GEO_LON']=float(row['GEO_LON'])
        row['GEO_LAT']=float(row['GEO_LAT'])
        if(row['DISTRICT_ID']!=''):
            row['DISTRICT_ID']=int(row['DISTRICT_ID'])
            
        else:
            row['DISTRICT_ID']=0
            

        if(row['PRECINCT_ID']!=''):
            
            row['PRECINCT_ID']=int(row['PRECINCT_ID'])
        else:
            
            row['PRECINCT_ID']=0            

        
        del row['BICYCLE_IND']
        del row['PEDESTRIAN_IND']
        data[id] = row
        #insert_request = requests.post(url="{}/{}/_doc/{}".format(es_url, es_index, row['OBJECTID_1']),
                                       #data=json.dumps(data[id]),
                                       #headers=post_request_headers).json()
        #print(insert_request)
        # print(row)

with open(json_path,'w')as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))


