import json
import os
import xmltodict

with open('input.xml') as xml_file:
    parsed_data = xmltodict.parse(xml_file.read())

    xml_file.close()

    json_conversion = json.dumps(parsed_data)
    
    with open('output.json', 'w') as json_file:
        
        if os.getenv("ENABLE"): 
            
            json_file.write(json_conversion)

            json_file.close()
        else:
            json_file.write("Env variable is not set")
            
            json_file.close()
