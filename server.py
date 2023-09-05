import numpy as np
import json
from licence import *

LICENCES_FILE_NAME = "licenses.json"
global licences
licences = []


def load_licences():
    try:
        with open(LICENCES_FILE_NAME) as file:
            json_data = json.load(file)["payload"]
            for item in json_data:
                licences.append(
                    Licence(item["LicenceUserName"],
                    int(item["ValidationTime"]),
                    item["LicenceKey"])
                )
    except FileNotFoundError:
        print("Licenses file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Invalid licenses file format.")
        exit(1)


if __name__ == "__main__":
    load_licences()
    
    port_number = 0
    try:
        port_number = int(input("Enter the port number:"))
    except ValueError:
        print("Port number must be a integer!")
        exit(1)
    if not (port_number > 0 and port_number < 65535):
        print("Invalid port number")
        exit(1)
        
    print(port_number)
    
