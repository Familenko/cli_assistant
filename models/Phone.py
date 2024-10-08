from models.Field import Field


class Phone(Field):
    def __init__(self, value):
        value = self.validate_phone(value)
        super().__init__(value)
    
    def validate_phone(self, value):
        # checking "+" symbol
        if value.startswith('+'):
            # delete of "+" before checking whether number consists of 10 symbols
            value = value[1:]
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number without the country code or with '+' followed by 10 numbers. Please, provide a correct phone number.")
        
        return value
