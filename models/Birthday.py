class Birthday:
 def __init__(self, value):
 super().__init__(value)
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please, use: DD.MM.YYYY")
