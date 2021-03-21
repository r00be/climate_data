import random as rd
import requests   #allows to send HTTP requests
import json       #allows to work with JSON file
import datetime as dt
import time

# each row of the field contain the static information of a node (field, sensor_id, longitude, latitude)
field1 = [[1,100,13.71145248413086,43.158361065027506], 
          [1,101,13.822174072265625,43.12604547425635], 
          [1,102,13.4307861328125,43.16311928246929], 
          [1,103,13.522796630859375,43.041794452901534],
          [1,104,13.23028564453125,43.06186472916744]]

field2 = [[2,105,13.872985839843748,42.67233920753351], 
          [2,106,13.7933349609375,42.48222557002593], 
          [2,107,13.45001220703125,42.6844544397102]]

field3 = [[3,108,13.1671142578125,43.644025847699496], 
          [3,109,12.859497070312498,43.42100882994726], 
          [3,110,13.38134765625,43.39107786275974],
          [3,111,13.172607421875,43.51270490464819]]
  

# Genereting data
def sensor_values():
  date = dt.datetime.now()
  epoch_time = time.time()

  if date.hour > 0 and date.hour < 4 or date.hour > 20:
    temp = rd.uniform(0,8) 
  else:
    temp = rd.uniform(8,15) 

  vwc = rd.uniform(0,1)   #Volumetric Water Content: numero randomico tra 0 e 1 (%)
  temp_soil = (float(temp) + rd.uniform(0, 1.5))  #slightly bigger or smaller than the enviroment temperature
  humidity = rd.uniform(0,100)

  vwc = round(vwc, 2)
  temp = round(temp, 2)
  temp_soil = round(temp_soil, 2)
  humidity = round(humidity, 2)

  list_values = [vwc,temp,temp_soil,humidity,epoch_time]

  return list_values

#3. Convert the data in JSON
def convert_to_json(list_values,i):
  
  x =  { "sensor_id": i[1], 
         "volumetric_water_content":list_values[0], 
         "temperature_enviroment": list_values[1], 
         "temperature_soil": list_values[2], 
         "percentage_humidity": list_values[3], 
         "acquisition_time": list_values[4]
        }
  y = json.dumps(x)

  return y

# 1. Infinite loop: for each field invokes the functions above
while True:

  list_json = []  #list of JSON 

  for i in  field1:
    
    #2. Collect the data generated
    list_values = sensor_values()

    #3. Convert the data in JSON
    dataJson = convert_to_json(list_values,i)

    list_json.append(dataJson)


  for i in  field2:


    list_values = sensor_values()
    dataJson = convert_to_json(list_values,i)

    list_json.append(dataJson)

  for i in  field3:

    list_values = sensor_values()
    dataJson = convert_to_json(list_values,i)

    list_json.append(dataJson)

  #4. Send the data to the API Gateway
  for i in list_json:

    payload = i
    headers = {}
    
    try:

      URL = 'https://gcm2ijz2qa.execute-api.us-east-1.amazonaws.com/dev/fields/nodes'

      response = requests.post(URL, payload, headers)  

      print(response.text)
    except:
      print("failed request")

  time.sleep(10)
