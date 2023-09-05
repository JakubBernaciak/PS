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
                    int(item["Licence"]),
                    int(item["ValidationTime"]),
                    item["IPadresses"]
                    )
                )
    except FileNotFoundError:
        print("Licenses file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Invalid licenses file format.")
        exit(1)


if __name__ == "__main__":
    load_licences()
    for licence in licences:
        if licence.number_of_licences > 1:
            print(licence.ipaddresses[1])
