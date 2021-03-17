import psycopg2 as ps
import time
import json

def lambda_handler(event, context):
    
    #1. Database connection
    
    try:
    
        conn = ps.connect(dbname='postgres',
                          user='postgres', 
                          host='db-gruppo1.cmgvpya5hdiu.us-east-1.rds.amazonaws.com', 
                          password='grouppo1ccs',
                          port = '5432')
        cur = conn.cursor()
    
        print("Connected to the database\n")
    
    except: 
        print("I am unable to connect to the database\n")
    
    print(event)
    
    #2. Takes the data from the "body" of event, which contains the field and the N minutes given in input
    data = json.loads(event["body"])

    field = data["field"]
    minutes = data["minutes"]
    
    time_now = time.time()     #The current epoch time 
    
    minutes = minutes*60
    minutes = float(time_now) - float(minutes)  
    
    #3. Select minimum, maximum and average of the data inside the database for each value
    query = "SELECT MIN(volumetric_water_content), MAX(volumetric_water_content), AVG(volumetric_water_content) FROM sensor_values INNER JOIN sensor_data ON sensor_values.sensor_id = sensor_data.sensor_id WHERE sensor_data.field = "+ str(field) +" AND sensor_values.acquisition_time BETWEEN "+ str(minutes) +" AND " + str(time_now) +" ;"
    cur.execute(query)
    result = cur.fetchall()     
    conn.commit()
    
    #4. Conversion of the result in JSON
    vwc = convert_to_json(result)   
    
    query = "SELECT MIN(temperature_enviroment), MAX(temperature_enviroment), AVG(temperature_enviroment) FROM sensor_values INNER JOIN sensor_data ON sensor_values.sensor_id = sensor_data.sensor_id WHERE sensor_data.field = "+ str(field) +" AND sensor_values.acquisition_time BETWEEN "+ str(minutes) +" AND " + str(time_now) +" ;"
    cur.execute(query) 
    result = cur.fetchall()
    conn.commit()
    
    envtemp = convert_to_json(result)
    
    query = "SELECT MIN(temperature_soil), MAX(temperature_soil), AVG(temperature_soil) FROM sensor_values INNER JOIN sensor_data ON sensor_values.sensor_id = sensor_data.sensor_id WHERE sensor_data.field = "+ str(field) +" AND sensor_values.acquisition_time BETWEEN "+ str(minutes) +" AND " + str(time_now) +" ;"
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    
    soiltemp = convert_to_json(result)
    
    query = "SELECT MIN(percentage_humidity), MAX(percentage_humidity), AVG(percentage_humidity) FROM sensor_values INNER JOIN sensor_data ON sensor_values.sensor_id = sensor_data.sensor_id WHERE sensor_data.field = "+ str(field) +" AND sensor_values.acquisition_time BETWEEN "+ str(minutes) +" AND " + str(time_now) +" ;"
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    
    humi = convert_to_json(result)
    
    cur.close()
    conn.close()
    
    #4. JSON containing the 4 json above and the relative field
    stats = {
        'volumetric_water_content' : vwc,
        'temperature_enviroment' : envtemp,
        'temperature_soil' : soiltemp,
        'percentage_humidity' : humi,
        'field' : field
    }
    
    #5. Return of the json with all the stats
    return { 
        'statusCode': 200,
        'body': (json.dumps(stats))
    }
    
#4. Function that converts the query's result in JSON
def convert_to_json(result):
    
    x = { 
    'min': result[0][0],  # result is a tuple inside a 1D list --> [(1, 2, 3)] needs the double index
    'max': result[0][1],
    'avg': round(result[0][2], 2)
    }

    y = json.dumps(x) 
    y = json.loads(y) 

    return y
