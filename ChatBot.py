from models.Addressbook import Addressbook
from models.Record import Record
from models.Birthday import Birthday 
from models.Email import Email 
from models.Field import Field
from models.Name import Name
from models.Phone import Phone

"""" class ChatBot:
    def __init__(self):
        self.commands = {"command-name": self.add_contact} #to replace with actual command names and funcs
        self.history = [command for command in self.commands] """

    def add_contact(args: list, book: AddressBook): 
        name, phone, email, *_ = args
    if Phone(phone):
        record = book.find(name)
        if not record:
            p = Record(Name(name))
            p.add_phone(phone)
            p.add_email(email)  
            book.add_record(p)
            print("Contact added.")
        else:
            record.add_phone(phone)
            record.add_email(email)  
            print("Contact updated.")
            print(book)
    else:
        raise ValueError("Invalid phone number.")

def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    if book.find(name):
        book[Record(name).name.value].append(birthday)
        print(book)

        print("Birthday added")
    else:
        record = Record(name)
        record.add_birthday(birthday)
        book.add_record(record)
        print(book)
        print("Birthday added")

    def add_phone(self, phone):
        record = self.book.find(name)
        if record:
            record.add_phone(phone)
        else:
            print(f"Contact {name} not found.")
        
    def add_email(self, name, email):
        record = self.book.find(name)
        if record:
            record.add_email(email)
        else:
            print(f"Contact {name} not found.")

    def add_notes(self):
        # TODO: add tages
        pass

    def delete_notes(self):
        pass

    def delete_contact(args:list, book: AddressBook):
        book.delete(args[0])
        print("Contact deleted")       

    def delete_phone(self, args: list):
        name, phone = args
        record = self.book.find(name)
        if record:
            record.remove_phone(phone)
            print(f"Phone {phone} deleted from contact {name}.")
        else:
            print(f"Contact {name} not found.")

   def delete_email(self, args: list):
        name = args[0]
        record = self.book.find(name)
        if record:
            record.email = None
            print(f"Email deleted from contact {name}.")
        else:
            print(f"Contact {name} not found.")

    def delete_birthday(self, args: list):
        name = args[0]
        record = self.book.find(name)
        if record:
            record.birthday = None
            print(f"Birthday deleted from contact {name}.")
        else:
            print(f"Contact {name} not found.")
            
    def edit_phone(self, old_phone, new_phone):                               
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone
        else:
            raise ValueError("Phone number not found")

    def edit_email(self, old_email, new_email):
        email_to_edit = self.find_email(old_email)
        if email_to_edit:
            email_to_edit.value = new_email
        else:
            raise ValueError("Email address not found")

    def edit_notes(self):
        pass

    def edit_birthday(self, name, new_birthday):
        record = self.book.find(name)
        if record:
            record.birthday = Birthday(new_birthday) 
            print(f"Birthday updated for contact {name} to {new_birthday}.")
        else:
            raise ValueError(f"Contact {name} not found.")

    def find_contact(self):
        pass

    def show_contacts(self):
        pass    

    def find_closest_birthday(self):
        pass

    def save_data(book: AddressBook, filename: str):
        with open(filename, "wb") as f:
             pickle.dump(book, f)

    def load_data(filename: str):
        try:
            with open(filename, "rb") as f:
                 return pickle.load(f)
        except FileNotFoundError:
            return AddressBook() 
