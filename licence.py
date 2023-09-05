import numpy as np

class Licence:
    def __init__(self, username: str,number_of_licences: int,validation_time: int,ipaddresses: np.array):
        self.username = username
        self.number_of_licences = number_of_licences
        self.validation_time = validation_time
        self.ipaddresses = np.copy(ipaddresses)
        