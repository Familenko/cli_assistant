from collections import UserDict
from datetime import datetime, timedelta
from utils.telegram import send_telegram_message
import pickle

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
        """Метод для серіалізації."""
        self.check_for_birthday()
        # Створюємо копію словника даних
        state = self.data.copy()
        return state

    def __setstate__(self, state):
        """Метод для десеріалізації."""
        self.data = state
        self.check_for_birthday()

    def save_to_file(self, filename):
        """Зберігає адресну книгу у файл."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_from_file(cls, filename):
        """Завантажує адресну книгу з файлу."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
