class Name:
    def __init__(self, value):
     if len(str(value)) < 2:
       raise ValueError("The requested name should consist of at least 2 letters. Please, use a different name")
     else: self.value = str(value).title()
