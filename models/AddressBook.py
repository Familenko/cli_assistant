from collections import UserDict
from datetime import datetime, timedelta
from utils.telegram import send_telegram_message


class AddressBook(UserDict):
    def add_record(self):
        pass

    def find_record(self):
        pass

    def delete_record(self):
        pass

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
        self.check_for_birthday()
        # TODO: подальша логіка для серіалізації

    def __setstate__(self, state):
        self.check_for_birthday()
        # TODO: подальша логіка для серіалізації
