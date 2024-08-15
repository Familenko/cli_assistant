from collections import UserDict
from models.Note import Note

class NoteBook(UserDict):
    def find_note(self, title):
        return self.data.get(title)

    def add_note(self, title):
        if self.find_note(title):
            raise ValueError("Note with this title already exists.")
        note = Note(title)
        self.data[title] = note

    def rename_note(self, old_title, new_title):
        note = self.find_note(old_title)
        if not note:
            raise ValueError("Note doesn't exist.")
        note.rename(new_title)
        self.data[new_title] = self.data.pop(old_title)

    def edit_note(self, title, text: list[str]):
        note = self.find_note(title)
        if not note:
            raise ValueError("Note doesn't exist.")
        note.edit_note(text)

    def delete_note(self, title):
        if not self.find_note(title):
            raise ValueError("Note doesn't exist.")
        del self.data[title]

    def __str__(self):
        return "\n".join([str(note) for note in self.data.values()])
