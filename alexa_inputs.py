class TemperatureIntentHandler(AbstractRequestHandler):
    """Handler for Temperature Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("itis_demo_temperature")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        #1. Takes the data from the given slots
        slots = handler_input.request_envelope.request.intent.slots   #percorso dati degli slots
        
        minutes = slots["minutes"].value
        field = slots["field"].value
        stat = slots["stat"].value
        temp = slots["temp"].value
        
        #2. GET request to the API of the JSON made by the min-max-avg function, sending the input needed
        url = "https://gcm2ijz2qa.execute-api.us-east-1.amazonaws.com/dev/fields/stats"
        
        headers = {}
        
        input_data = {
                'field' : field,        #field of the ndoes
                'minutes' : minutes     #last n minutes to refer to
        }
        
        payload = json.dumps(input_data)      #JSON string of 'input_data'
        
        response = requests.request("GET", url, headers=headers, data=payload)
        
        data=json.loads(response.text)  #dictionary of 'response'
        
        #3.0 Checks what the slot's value is (node's data), in order to take the right dictionary
        if (temp == "temperatura ambientale" or temp == "temperatura" or temp == "temperatura ambiente"):
            x = "temperature_enviroment"

        if (temp == temp == "temperatura del suolo" or temp == "temperatura suolo"):
            x = "temperature_soil"

        if (temp == "contenuto volumetrico d'acqua" or temp == "contenuto volumetrico dell'acqua" or temp == "cva" or temp == "vwc"):
            x = "volumetric_water_content"
            
        if (temp == "umidità"):
            x = "percentage_humidity"

        #3.1 Checks what the slot's value is (min,max or avg), in order to take the right dictionary
        if(stat == "minimo" or stat == "minima"):
            y = "min"
            
        if(stat == "massimo" or stat == "massima"):
            y = "max"
            
        if(stat == "media"):
            y = "avg"

        #4. Takes the result from the dictionaries above of 'data'
        result = data[""+x+""][""+y+""]
        
        #5. Output of the result
        speak_output = "negli ultimi "+ str(minutes) +" minuti, nel campo "+ str(field) +" la "+ str(temp) +" "+ str(stat) +" è: "+ str(result) +"."

        return (
                handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
