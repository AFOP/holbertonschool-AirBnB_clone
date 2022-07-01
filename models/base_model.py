#!/usr/bin/python3
# defines all common attributes/methods for other classes


import uuid
from datetime import datetime

class BaseModel:
    # class BaseModel

    def __init__(self):
    # method constructor

        self.id = str(uuid.uuid4())
        self.created_at = (datetime.now()).strftime('%d/%m/%Y %H:%M')
        

base = BaseModel()
print(base.id)
print(base.created_at)
