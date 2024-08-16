from collections import UserDict
from datetime import datetime, timedelta
import pickle

from utils.telegram import send_telegram_message
from models.Record import Record
from models.Name import Name
from models.Phone import Phone
from models.Birthday import Birthday
from models.Adress import Adress
from models.Email import Email


class AddressBook(UserDict):
    def add_record(self, record):
        """Додає новий запис до адресної книги."""
        self.data[record.name.value] = record

    def find_record(self, name):
        """Знаходить запис за ім'ям."""
        return self.data.get(name)

    def delete_record(self, name):
        """Видаляє запис за ім'ям."""
        if name in self.data:
            del self.data[name]
            return True
        return False

    def get_upcoming_birthdays(self, days: int = 7):
        today = datetime.now().date()
        deadline = today + timedelta(days=days)
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday = birthday.replace(year=today.year)
                if today <= birthday <= deadline:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

    def check_for_birthday(self):
        upcoming_birthdays = self.get_upcoming_birthdays()
        newbirthday_people = [record.name.value for record in upcoming_birthdays]
        for man in newbirthday_people:
            message = f"Цього тижня ми вітаємо з днем народження {man}!"
            send_telegram_message(message)

    def __getstate__(self):
        # to send a message about upcoming birthdays during saving
        self.check_for_birthday()

        state = {}
        for name, record in self.data.items():
            state[name] = {
                'name': name,
                'phones': [phone.value for phone in record.phones],
                'birthday': record.birthday.value if record.birthday else None,
                'address': record.address.value if record.address else None,
                'email': [email.value for email in record.emails],
            }

        return state

    def __setstate__(self, state):
        # to send a message about upcoming birthdays during loading
        self.check_for_birthday()

        self.data = state

        self.data = {}
        for name, record in state.items():
            new_record = Record(name)
            new_record.phones = [Phone(phone) for phone in record['phones'] if phone]
            new_record.birthday = Birthday(record['birthday']) if record['birthday'] else None
            new_record.address = Adress(record['address']) if record['address'] else None
            new_record.emails = [Email(email) for email in record['email'] if email]
            new_record.name = Name(name)

            self.data[name] = new_record

    def save_to_file(self, filename):
        """Зберігає адресну книгу у файл."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_from_file(cls, filename):
        """Завантажує адресну книгу з файлу."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
