class Phone:
    def __init__(self, value):
     super().__init__(value)
     if not value.isdigit() or len(value) != 10:
       raise ValueError("Phone number must be a 10-digit number. Please, provide a correct phone number")
