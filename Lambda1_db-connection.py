import json                 #allows to work with JSON files
import psycopg2 as ps       #allows to work with PostgreSQL database


def lambda_handler(event, context):
    # TODO implement

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
    
    
    #2. Takes the data from the "body" of event
    data = json.loads(event["body"])
    
    sensor_id = data["sensor_id"]
    volumetric_water_content = data["volumetric_water_content"]
    temperature_enviroment = data["temperature_enviroment"]
    temperature_soil = data["temperature_soil"]
    percentage_humidity = data["percentage_humidity"]
    acquisition_time = data["acquisition_time"]
    
    
    #3. Inserting the data taken from the nodes into the database
    query = "INSERT INTO sensor_values(sensor_id, volumetric_water_content, temperature_enviroment, temperature_soil, percentage_humidity, acquisition_time) VALUES (%s, %s, %s, %s, %s, %s);"
    query_request = (sensor_id, volumetric_water_content, temperature_enviroment, temperature_soil, percentage_humidity, acquisition_time)
    cur.execute(query, query_request)
    conn.commit()
    cur.close()
    conn.close()
    
    return { 
        'statusCode': 200,
        'body': str(data)
    }
    
