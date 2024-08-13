from models.Name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.emails = []
        self.notes = []

    def add_phone(self, phone):
        pass

    def edit_phone(self, phone):
        pass

    def delete_phone(self, phone):
        pass

    def add_birthday(self, birthday):
        pass

    def edit_birthday(self, birthday):
        pass

    def delete_birthday(self, birthday):
        pass

    def add_email(self, email):
        pass

    def edit_email(self, email):
        pass

    def delete_email(self, email):
        pass

    def add_notes(self, notes):
        pass

    def edit_notes(self, notes):
        pass

    def delete_notes(self, notes):
        pass
