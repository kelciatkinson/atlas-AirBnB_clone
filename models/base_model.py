#!/usr/bin/python3
import uuid

class BaseModel():
    
    def __init__(self, id=None):
        self.id = uuid.uuid4()

