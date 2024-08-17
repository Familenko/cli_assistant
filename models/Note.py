from models.Content import Content
from models.Title import Title

class Note:
    def __init__(self, title):
        self.title = Title(title)
        self.content = Content("")

    def rename(self, new_title):
        self.title = Title(new_title)

    def edit_note(self, content: str):
        self.content = Content(content)

    def __str__(self):
        return f"Title: {self.title.value}\nText: " + ("(note appears to be empty)" if self.content.value == "" else "\n" + self.content.value)
