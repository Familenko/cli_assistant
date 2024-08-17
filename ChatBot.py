import pickle
from tabulate import tabulate

from models.AddressBook import AddressBook
from models.Record import Record
from models.Birthday import Birthday 
from models.Email import Email 
from models.Phone import Phone
from models.Email import Email

class ChatBot:
    def __init__(self, book: AddressBook = AddressBook()):
        self.book = book
        self.commands = {"add": self.add_contact,
                "add-phone": self.add_phone,
                "change-phone": self.edit_phone,
                "add-email": self.add_email,
                "change-email": self.edit_email,
                "delete": self.delete_contact,
                "delete-phone": self.delete_phone,
                "delete-email": self.delete_email,
                "add-birthday": self.add_birthday,
                "edit-birthday": self.edit_birthday,
                "delete-birthday": self.delete_birthday,
                "show": self.find_contact,
                "all": self.show_contacts,
                "birthdays": self.find_closest_birthday,
                "add-note": self.add_notes,
                "edit-note": self.edit_notes,
                "delete-note": self.delete_notes}
        self.history = [command for command in self.commands]

    def add_contact(self, args: list): 
         #add John 1234567890 example@email.com 20.08.2000
        name, phone, email, birthday, *_ = args
        record = self.book.find_record(name)
        if not record:
            record = Record(name)
            record.add_phone(phone) if phone else None
            record.add_email(email) if email else None
            record.add_birthday(birthday) if birthday else None
            self.book.add_record(record)
            print(f"Contact {name} added")
        else: 
            return record

    def add_phone(self, args):
        #add-phone John 1234567890
        name, phone, *_ = args
        record = self.book.find_record(name)
        if not record:
            record = Record(name)
            record.add_phone(phone)
            self.book.add_record(record)
        else: self.book[name].add_phone(phone)
        print(f"Phone number added for {name}")
        
    def edit_phone(self, args):   
        #change-phone John 2223334441 5553334440
        name, old_phone, new_phone, *_ = args                          
        record = self.book.find_record(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            print(f"Phone number updated for {name}")
        else: 
            print(f"Contact name {name} not found in contacts")

    def add_email(self, args):
        #add-email John example@ex.com
        name, email, *_ = args
        record = self.book.find_record(name)
        if not record:
            record = Record(name)
            record.add_email(email)
            self.book.add_record(record)
        else: self.book[name].add_email(email) 
        print(f"Email added for {name}")
        
    def edit_email(self, args):
        #change-email John example@example.com test@test.com
        name, old_email, new_email, *_ = args
        record = self.book.find_record(name)
        if record:
            record.edit_email(old_email, new_email)
            print(f"Email updated for {name}")
        else: 
            print(f"Contact name {name} not found in contacts")

    def delete_contact(self, args):
        #delete John
        name, *_ = args
        if name not in self.data:
            print(f"Contact name {name} not found in contacts")
        else:
            self.book.delete_record(name)
            print("Contact deleted")       

    def delete_phone(self, args: list):
        #delete-phone John 1234567888
        name, phone, *_ = args
        record = self.book.find_record(name)
        if not record:
            print(f"Contact name {name} not found in contacts")
        else:
            if phone in self.book[name].phones:
                self.book[name].delete_phone(phone) #поки що так
                print(f"Phone {phone} deleted for contact {name}")
            else:
                print("Phone number not found in contacts list")
       
    def delete_email(self, args: list):
        # delete John ex@example.com
        name, email, *_ = args
        if not self.book.find_record(name):
            print(f"Contact name {name} not found in contacts")
        else:
            if email in self.book[name].emails:
                self.book[name].delete_email(email) 
                print(f"Email {email} deleted for contact {name}")
            else:
                print("Email not found in contacts list")
         
    def add_birthday(self, args):
        # add-birthday John 10.10.2000
        name, birthday, *_ = args
        if not self.book.find_record(name):
            print(f"Contact name {name} not found in contacts")
        if self.book[name].birthday:
            self.book[name].edit_birthday(birthday)
        else:
            self.book[name].add_birthday(birthday)
            print(f"Birthday added for {name}")

    def edit_birthday(self, args):
        # edit-birthday John 21.10.1999
        name, new_birthday, *_ = args
        if self.book[name].birthday:
            self.book[name].edit_birthday(new_birthday)
        else:
            self.book[name].add_birthday(new_birthday)
        print(f"Birthday updated for contact {name}")
   
    def delete_birthday(self, args: list):
        # delete-birthday John
        name, *_ = args
        if self.book.find_record(name):
            self.book[name].birthday = None
            print(f"Birthday deleted")
        else:
            print(f"Contact name {name} not found in contacts")

    def find_contact(self, args):
        #show John
        name, *_ = args
        record = self.book.find_record(name)
        record = self.book.find_record(name).__dict__
        data = {str(k):str(v) for k, v in record.items() if k!="notes"}
        table_data = list()
        table_data.append(data)
        print(tabulate(table_data, headers="keys", tablefmt="grid"))
#TO_REMOVE IF TABLE WORKS CORRECTLY:
        # for name, values in record.__dict__.items():
        #     print(str(name), str(values))

    def show_contacts(self):
        # #command: all
        table_data = list()
        for record in self.book.values():
            table_data.append({str(k):str(v) for k, v in record.__dict__.items() if k!="notes"})
        print(tabulate(table_data, headers="keys", tablefmt="grid"))
#TO_REMOVE IF TABLE WORKS CORRECTLY:
        # for record in self.book.values():
        #     for name, values in record.__dict__.items():
        #         print(f"{str(name)}: {str(values)} ", end = '')
        #     print("")
    def find_closest_birthday(self):
        #command: birthdays
        birthdays = self.book.get_upcoming_birthdays()
        table_data = list()
        headers = ["Name", "Birthday"]
        for birthday in birthdays:
            table_data.append((birthday.name, birthday.birthday))
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
#TO-REMOVE IF TABLE WORKS CORRECTLY:
        # birthdays = self.book.get_upcoming_birthdays()
        # for birthday in birthdays:
        #     print(birthday.name, birthday.birthday)

    def add_notes(self):
        #command: add-note
        #далі - текст ноута
        #наразі add_notes() метод знаходиться в класі Record, де атрибут Name - 
        #обов'язковий, а для ноутів він нам не треба. Переробити
        pass
                
    def edit_notes(self):
    
        pass

    def delete_notes(self):
        #same as above
        pass

    @staticmethod
    def save_data(filename: str, book: AddressBook = AddressBook()):
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(filename: str):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()
        