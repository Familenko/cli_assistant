import pickle

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
        record = Record(name)
        if not self.book.find_record(name):
            record.add_phone(phone) if phone else None
            record.add_email(email) if email else None
            record.add_birthday(birthday) if birthday else None
            self.book.add_record(record)
            print("Contact added")
        else: #ПЕРЕРОБИТИ
            if record.phones:
                record.phones.append(phone)
                print("One more phone number added")
            if record.emails:
                record.emails.append(email)
                print("One more email added")
            if record.birthday:
                record.birthday = birthday
                print("Birthday updated")

    def add_phone(self, args):
        #add-phone John 1234567890
        name, phone, *_ = args
        if not self.book.find_record(name):
            record = Record(name)
            record.add_phone(phone)
            self.book.add_record(record)
        else: self.book[name]["phone"] = Phone(phone).value 
        #поки що так, коли буде готовий AddressBook, перероблю
        
    def edit_phone(self, args):   
        #change-phone John 2223334441 5553334440
        name, old_phone, new_phone, *_ = args                          
        record = Record(name)
        record.edit_phone(old_phone, new_phone)
        
    def add_email(self, args):
        #add-email John example@ex.com
        name, email, *_ = args
        if not self.book.find_record(name):
            record = Record(name)
            record.add_email(email)
            self.book.add_record(record)
        else: self.book[name]["email"] = Email(email).value #поки що так, коли буде готовий AddressBook, перероблю
        
    def edit_email(self, args):
        #change-email John example@example.com test@test.com
        name, old_email, new_email, *_ = args
        record = Record(name)
        record.edit_email(old_email, new_email)

    def delete_contact(self, args):
        #delete John
        name, *_ = args
        if name not in self.data:
            print("Name not found in contacts")
        else:
            self.book.delete_record(name)
            print("Contact deleted")       

    def delete_phone(self, args: list):
        #delete-phone John 1234567888
        name, phone, *_ = args
        if not self.book.find_record(name):
            print("Name not found in contacts")
        else:
            if phone in self.book[name]["phone"]:
                self.book[name]["phone"].remove(phone) #поки що так
                print(f"Phone {phone} deleted from contact {name}.")
            else:
                print("Phone not found")
       
    def delete_email(self, args: list):
        # delete John ex@example.com
        name, email, *_ = args
        if not self.book.find_record(name):
            print(f"Contact {name} not found.")
        else:
            if email in self.book[name]["email"]:
                self.book[name]["email"].remove(email) #поки що так
                print(f"Email {email} deleted from contact {name}.")
            else:
                print("Email not found")
         
    def add_birthday(self, args):
        # add-birthday John 10.10.2000
        name, birthday, *_ = args
        if not self.book.find_record(name):
            print("Name not found in contacts")
        if self.book[name]["birthday"]:
            print("This person already has a birthday record.")
        else:
            self.book[name]["birthday"] = Birthday(birthday).value
            print("Birthday added")

    def edit_birthday(self, args):
        # edit-birthday John 21.10.1999
        name, new_birthday, *_ = args
        if self.book[name]["birthday"]:
            self.book[name]["birthday"] = new_birthday
        else:
            self.book[name]["birthday"] = Birthday(new_birthday).value
        print(f"Birthday updated for contact {name} to {new_birthday}.")
   
    def delete_birthday(self, args: list):
        # delete-birthday John
        name, *_ = args
        if self.book.find_record(name):
            del self.book[name]["birthday"]
        else:
            print(f"Contact {name} not found.")

    def find_contact(self, args):
        #show John
        name, *_ = args
        self.book.find_record(name)

    def show_contacts(self):
        #command: all
        for name, records in self.book.items():
            print(name, records)

    def find_closest_birthday(self):
        #command: birthdays
        self.book.get_upcoming_birthdays()

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

    