import re

class Email:
    super().__init__(value)
    def __init__(self, value):
        self.value = self.validate_email(value)
    
    def validate_email(self, value):
        if len(value) < 5:
            raise ValueError("The email address should be at least 5 characters long.")
        
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, value):
            raise ValueError("The provided email address is not valid. Please, use a valid email.")
        
        return value
