from datetime import datetime
from models.Field import Field


class Birthday(Field):
 def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Please, use: DD.MM.YYYY")
