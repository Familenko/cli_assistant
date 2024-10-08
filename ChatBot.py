import pickle
from prompt_toolkit import prompt
from tabulate import tabulate

from models.AddressBook import AddressBook
from models.NoteBook import NoteBook
from models.Record import Record
from models.Birthday import Birthday 
from models.Email import Email 
from models.Phone import Phone
from models.Email import Email
from models.AddressBook import AddressBook
from models.NoteBook import NoteBook


class ChatBot:
    def __init__(self):
        self.book, self.notebook = self.load_data()

        self.commands = {
            "help": self.help,

            "add-contact": self.add_contact,
            "delete-contact": self.delete_contact,
            "find-contact": self.find_contact,
            "show-contacts": self.show_contacts,

            "add-phone": self.add_phone,
            "edit-phone": self.edit_phone,
            "delete-phone": self.delete_phone,

            "add-email": self.add_email,
            "delete-email": self.delete_email,
            "edit-email": self.edit_email,

            "add-birthday": self.add_birthday,
            "edit-birthday": self.edit_birthday,
            "delete-birthday": self.delete_birthday,
            "find-closest-birthday": self.find_closest_birthday,

            "add-address": self.add_address,
            "edit-address": self.edit_address,
            "delete-address": self.delete_address,

            "find-note": self.find_note,
            "add-note": self.add_note,
            "show-notes": self.show_all_notes,
            "rename-note": self.rename_note,
            "edit-note": self.edit_note,
            "delete-note": self.delete_note,

            "add-tag-to-note": self.add_tag_to_note,
            "remove-tag-from-note": self.remove_tag_from_note,
            "search-notes-by-tag": self.search_notes_by_tag,
            "sort-notes-by-tags": self.sort_notes_by_tags,
            }
        
        self.history = [command for command in self.commands]

    def help(self, *args):
        print("Here is the list of available commands:")
        for command in self.commands.keys():
            print(command)

    def add_contact(self, *args):
        match len(args):
            case 1:
                name, *_ = args
                phone, email, birthday, address = None, None, None, None
            case 2:
                name, phone, *_ = args
                email, birthday, address = None, None, None
            case 3:
                name, phone, email, *_ = args
                birthday, address = None, None
            case 4:
                name, phone, email, birthday, *_ = args
                address = None
            case 5:
                name, phone, email, birthday, address, *_ = args

        record = self.book.find_record(name)
        if not record:
            record = Record(name)
            record.add_phone(phone) if phone else None
            record.add_email(email) if email else None
            record.add_birthday(birthday) if birthday else None
            record.add_address(address) if address else None
            self.book.add_record(record)
            print(f"Contact {name} added")
        else: 
            print(f"Contact {name} already exists")

    def add_phone(self, *args):
        name, phone, *_ = args
        record = self.book.find_record(name)
        if record:
            record.add_phone(phone)
            print(f"Phone number added for {name}")
        else:
            print(f"Contact name {name} not found in contacts")
        
    def edit_phone(self, *args):   
        name, old_phone, new_phone, *_ = args                          
        record = self.book.find_record(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            print(f"Phone number updated for {name}")
        else: 
            print(f"Contact name {name} not found in contacts")

    def add_email(self, *args):
        name, email, *_ = args
        record = self.book.find_record(name)
        if record:
            record.add_email(email)
            print(f"Email added for {name}")
        else:
            print(f"Contact name {name} not found in contacts")
        
    def edit_email(self, *args):
        name, old_email, new_email, *_ = args
        record = self.book.find_record(name)
        if record:
            record.edit_email(old_email, new_email)
            print(f"Email updated for {name}")
        else: 
            print(f"Contact name {name} not found in contacts")

    def delete_contact(self, *args):
        name, *_ = args
        record = self.book.find_record(name)
        if record:
            self.book.delete_record(name)
            print(f"Contact {name} deleted")
        else:
            print(f"Contact name {name} not found in contacts")  

    def delete_phone(self, *args):
        name, phone, *_ = args
        record = self.book.find_record(name)
        if record:
            record.delete_phone(phone)
            print(f"Phone number deleted for {name}")
        else:
            print(f"Contact name {name} not found in contacts")
       
    def delete_email(self, *args):
        name, email, *_ = args
        record = self.book.find_record(name)
        if record:
            record.delete_email(email)
            print(f"Email deleted for {name}")
        else:
            print(f"Contact name {name} not found in contacts")
         
    def add_birthday(self, *args):
        name, birthday, *_ = args
        record = self.book.find_record(name)
        if record:
            record.add_birthday(birthday)
            print(f"Birthday added for {name}")
        else:
            print(f"Contact name {name} not found in contacts")

    def edit_birthday(self, *args):
        name, new_birthday, *_ = args
        if self.book[name].birthday:
            self.book[name].edit_birthday(new_birthday)
            print(f"Birthday updated for contact {name}")
        else:
            print(f"Contact name {name} not found in contacts")
   
    def delete_birthday(self, *args):
        name, *_ = args
        if self.book.find_record(name):
            self.book[name].birthday = None
            print(f"Birthday deleted")
        else:
            print(f"Contact name {name} not found in contacts")

    def add_address(self, *args):
        name, address, *_ = args
        record = self.book.find_record(name)
        if record:
            record.add_address(address)
            print(f"Address added for {name}")
        else:
            print(f"Contact name {name} not found in contacts")

    def edit_address(self, *args):
        name, new_address, *_ = args
        if self.book[name].address:
            self.book[name].edit_address(new_address)
            print(f"Address updated for contact {name}")
        else:
            print(f"Contact name {name} not found in contacts")

    def delete_address(self, *args):
        name, *_ = args
        if self.book.find_record(name):
            self.book[name].address = None
            print(f"Address deleted")
        else:
            print(f"Contact name {name} not found in contacts")

    def find_contact(self, *args):
        name, *_ = args
        record = self.book.find_record(name)
        data = {
            "Name": record.name.value,
            "Phones": ", ".join([phone.value for phone in record.phones]),
            "Birthday": record.birthday.value if record.birthday else "",
            "Emails": ", ".join([email.value for email in record.emails]),
            "Address": record.address.value if record.address else ""
        }
        table_data = [data]
        print(tabulate(table_data, headers="keys", tablefmt="grid"))

    def show_contacts(self):
        table_data = []
        for record in self.book.values():
            record_data = {
                "Name": record.name.value,
                "Phones": ", ".join([phone.value for phone in record.phones]),
                "Birthday": record.birthday.value if record.birthday else "",
                "Emails": ", ".join([email.value for email in record.emails]),
                "Address": record.address.value if record.address else "",
            }
            table_data.append(record_data)

        print(tabulate(table_data, headers="keys", tablefmt="grid"))

    def find_closest_birthday(self):
        birthdays = self.book.get_upcoming_birthdays()
        table_data = list()
        headers = ["Name", "Birthday"]
        for man in birthdays:
            table_data.append((man.name, man.birthday))

        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        self.book.check_for_birthday()

    def add_note(self, *args):
        title, *_ = args
        self.notebook.add_note(title)
                
    def find_note(self, *args):
        title, *_ = args
        note = self.notebook.find_note(title)
        if not note:
            raise ValueError("Note doesn't exist.")
        print(note)
        print("Tags: " + (", ".join(self.notebook.tags.get_tags_for_note(note.title.value)) or "(no tags assigned)"))
      
    def show_all_notes(self):
        print(self.notebook)

    def rename_note(self, *args):
        old_title, new_title, *_ = args
        self.notebook.rename_note(old_title, new_title)

    def edit_note(self, *args):
        title, *_ = args
        note = self.notebook.find_note(title)
        if not note:
            raise ValueError("Note doesn't exist.")
        content = prompt(f"Editing note '{title}'. Press (Alt+Enter) to finish editing:\n", multiline=True, default=note.content.value)
        note.edit_note(content)

    def delete_note(self, *args):
        title, *_ = args
        self.notebook.delete_note(title)

    def add_tag_to_note(self, *args):
        title, tag, *_ = args
        self.notebook.add_tag(title, tag)

    def remove_tag_from_note(self, *args):
        title, tag, *_ = args
        self.notebook.remove_tag(title, tag)

    def search_notes_by_tag(self, *args):
        tag, *_ = args
        notes = self.notebook.tags.get_notes_by_tag(tag)
        if notes:
            for note in notes:
                print(note)
        else:
            print("(no notes found)")

    def sort_notes_by_tags(self):
        sorted_titles = self.notebook.tags.sort_notes_by_tags(self.notebook.keys())
        if sorted_titles:
            for title in sorted_titles:
                note = self.notebook.find_note(title)
                print(note)
                print("Tags: " + (", ".join(self.notebook.tags.get_tags_for_note(note.title.value)) or "(no tags assigned)"))
        else:
            print("(notebook appears to be empty)")

    def save_data(self, addressbook_file="addressbook.pkl", notebook_file="notebook.pkl"):
        with open(addressbook_file, 'wb') as file:
            pickle.dump(self.book, file)

        with open(notebook_file, 'wb') as file:
            pickle.dump(self.notebook, file)

    def load_data(self, addressbook_file="addressbook.pkl", notebook_file="notebook.pkl"):
        try:
            with open(addressbook_file, "rb") as f:
                book = pickle.load(f)
        except FileNotFoundError:
            book = AddressBook()

        try:
            with open(notebook_file, "rb") as f:
                notebook = pickle.load(f)
        except FileNotFoundError:
            notebook = NoteBook()

        return book, notebook
