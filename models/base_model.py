#!/usr/bin/python3
import uuid

class BaseModel():
    
    def __init__(self, id=None):
        self.id = uuid.uuid4()

#!/usr/bin/python3
"""Base model class for AirBnB - The Console
"""
import uuid
from datetime import datetime


class Base:
    """Base Model Class"""
    
    def __init__(self, *args, **kwargs):
        """Base Model Class Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, %Y-%m-%dT%H:%M:%S.%f)
                else:
                    
    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):





