import random as rd
import requests   #allows to send HTTP requests
import json       #allows to work with JSON file

#codes of the "nodes" from the provinces' capitals of the Marche

Ancona = 223
Ascoli_Piceno = 373
Fermo = 2743
Macerata = 3733
Pesaro = 5097
Urbino = 7535

list_nodes = [Pesaro,Urbino,Ancona,Macerata,Fermo,Ascoli_Piceno] #the codes are listed

#1. returns the json data of the nodes' code from the Corriere website
def request_json(node_code):

  payload = {}
  headers = {}
  URL = "https://meteo.corriere.it/meteoapi.php?c=" + str(node_code) #URL of the website

  try:
    response = requests.request("GET", URL, headers=headers, data=payload)
    dataJson = json.loads(response.text) # response.text ==> Json (type Dictionary)
    return dataJson
  except:
    print("ERRORE: connesione non riuscita")

list_json = [] #list of the json dat (initialize)

#while True:

for i in  list_nodes:

    node_code = i
    json_data = request_json(node_code)

    #2. Construct the body of the response
    id = json_data["lid"]
    field = json_data["nome"]
    vwc = rd.uniform(0,1)   #Volumetric Water Content: not present in the json, so it is a random number between 0 and 1
    vwc = str(round(vwc, 2))
    temp = json_data["temperatura"] 
    temp_soil = (float(temp) +rd.uniform(-1.5, 1.5))  #not present in the json, so it is slightly bigger or smaller than the enviroment temperature
    temp_soil = str(round(temp_soil, 2))
    humidity = json_data["umidita_relativa"]
    lat = json_data["lat"]
    lon = json_data["lon"]
    date = json_data["ora_unix"]

    x =  '{ "id":"'+id+'", "field":"'+field+'", "vwc":"'+str(vwc)+'", "temp":"'+temp+'", "temp_suolo":"'+str(temp_soil)+'", "humidity":"'+humidity+'", "lat":"'+lat+'", "lon":"'+lon+'", "date":"'+date+'"}'
    y = json.loads(x)

    list_json.append(y)
    
#time.sleep(10)
