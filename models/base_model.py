#!/usr/bin/python3
import uuid

class BaseModel():
    
    def __init__(self, id=None):
        self.id = uuid.uuid4()

#!/usr/bin/python3
"""Base model class for AirBnB - The Console
"""


class Base:
    """Base Model Class"""
    def __init__(self):
        """Base Model Class Initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, %Y-%m-%dT%H:%M:%S.%f)


