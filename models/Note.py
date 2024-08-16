from models.Content import Content
from models.Title import Title

class Note:
    def __init__(self, title):
        self.title = Title(title)
        self.content = []

    def rename(self, new_title):
        self.title = Title(new_title)

    def edit_note(self, content: list[str]):
        self.content = [Content(line) for line in content]

    def add_line(self, line):
        self.content.append(Content(line))

    def remove_line(self, line_number):
        del self.content[line_number]

    def edit_line(self, line_number, new_line):
        self.content[line_number] = Content(new_line)

    def __str__(self):
        return f"Title: {self.title.value}\nText: " + ("(note appears to be empty)" if not self.content else "\n" + "\n".join(line.value for line in self.content))
