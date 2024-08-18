from models.Field import Field


class Address(Field):
    def __init__(self, value):
        if value.isascii() and value.isalpha():
            super().__init__(value)
        else:
            raise ValueError("Adress must be a string of printable ASCII characters.")
