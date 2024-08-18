from models.Name import Name
from models.Phone import Phone
from models.Birthday import Birthday
from models.Address import Address
from models.Email import Email


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.emails = []
        self.notes = []
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Old phone number not found")

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def add_birthday(self, birthday):
        if self.birthday:
            raise ValueError("Birthday already exists")
        self.birthday = Birthday(birthday)

    def edit_birthday(self, new_birthday):
        if not self.birthday:
            raise ValueError("Birthday does not exist")
        self.birthday = Birthday(new_birthday)

    def delete_birthday(self):
        if not self.birthday:
            raise ValueError("Birthday does not exist")
        self.birthday = None

    def add_email(self, email):
        self.emails.append(Email(email))

    def edit_email(self, old_email, new_email):
        for email in self.emails:
            if email.value == old_email:
                email.value = new_email
                return
        raise ValueError("Old email not found")

    def delete_email(self, email):
        self.emails = [e for e in self.emails if e.value != email]

    def add_address(self, address):
        if self.address:
            raise ValueError("Address already exists")
        self.address = Address(address)

    def edit_address(self, new_address):
        if not self.address:
            raise ValueError("Address does not exist")
        self.address = Address(new_address)

    def delete_address(self):
        if not self.address:
            raise ValueError("Address does not exist")
        self.address = None
