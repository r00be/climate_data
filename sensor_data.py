import random as rd
import requests   #permette di inviare richieste HTTP
import json       #permette di lavorare con i dati JSON
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import time
#inizializzazione delle variabili

'''
LAquila = "3422"
Aosta = "266"
Ancona = "223"
Bari = "533"
Bologna = "745"
Campobasso = "1176"
Cagliari = "1039"
Catanzaro = "1833"
Firenze = "2798"
Genova = "3088"
Milano = "4074"
Napoli = "4579"
Palermo = "4937"
Perugia = "5096"
Potenza = "5483"
Roma = "5913"
Torino = "7301"
Trento= "7429"
Trieste = "7468"
Venezia = "7729"
'''
'''
Ancona = "223"
Ascoli_Piceno = "373"
Fermo = "2743"
Macerata = "3735"
Pesaro = "5097"
Urbino = "7535"
'''
'''
timeline = ["00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30","04:00","04:30","05:00","05:30",
            "06:00","06:30","07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30",
            "12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30",
            "18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30","24:00"]
'''

#campo_sensore = input("Scegli regione: ")

payload = {}
headers = {}

#legge il codice della città, affinché sia un numero intero
node_code = input("\nInserisci codice-città da ricercare\n> ")
URL = "https://meteo.corriere.it/meteoapi.php?c=" + str(node_code) #URL del corriere
try:
  response = requests.request("GET", URL, headers=headers, data=payload)
  dataJson = json.loads(response.text) # response.text ==> Json (tipo Dizionario)
except:
  print("ERRORE: '" + str(node_code) + "' è una richiesta non accettata")

data = dt.datetime.now()
lat = dataJson["lat"]
lon = dataJson["lon"]
città = dataJson["nome"]
id = dataJson["lid"]
temp = dataJson["temperatura"] #restituisce la temperatura
temp_suolo = (float(temp) +rd.uniform(-1.5, 1.5))
umidità = dataJson["umidita_relativa"]
print("Id: ", id)
print("Data: ", data)
print("latitudine: ", lat)
print("longitudine: ", lon)
print("Città: ", città)
print("Temperatura: ", temp)
print("Temperatura suolo: ", temp_suolo)
print("Umidità: ", umidità)

timeline = []
list_temp = []
list_umi = []
list_temp_suolo = []

k = 0

while k<=24:
  num_temp = rd.uniform(-0.2, 1) 
  num_temp_suolo = num_temp + rd.uniform(-0.2, 0.2) 
  if k > 0 and k < 5 or k > 13:
    temp = float(temp) - num_temp
    temp_suolo = float(temp_suolo) - num_temp_suolo
  else:
    temp = float(temp) + num_temp
    temp_suolo = float(temp_suolo) + num_temp_suolo
  timeline.append(k)
  list_temp.append(temp)
  list_umi.append(umidità)
  list_temp_suolo.append(temp_suolo)
  k += 0.5

#### PLOTTING ####
plt.title(città)

plt.subplot(2, 1, 1)
plt.plot(timeline, list_temp, '.-', color = 'red')
plt.plot(timeline, list_temp_suolo, color = 'brown')
plt.xlabel("timeline")
plt.ylabel("temperature °C")

plt.subplot(2, 1, 2)
plt.plot(timeline, list_umi, color = 'green')
plt.xlabel("timeline")
plt.ylabel("humidity %")
'''
plt.subplot(3, 1, 3)

plt.xlabel("timeline")
plt.ylabel("ground temperature °C")
plt.plot(timeline, list_temp_suolo, color = 'brown')'''
plt.show()
