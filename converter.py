import json
import xmltodict

with open('input.xml') as xml_file:
    parsed_data = xmltodict.parse(xml_file.read())

    xml_file.close()

    json_conversion = json.dumps(parsed_data)
    
    if os.getenv("ENABLE"): 
        with open('output.json', 'w') as json_file:
            json_file.write(json_conversion)

            json_file.close()
    else:
        print("Env variable is not set")
