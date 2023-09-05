import numpy as np

class Licence:
    def __init__(self, username: str, validation_time: int,key: str):
        self.username = username
        self.validation_time = validation_time
        self.key = key
        