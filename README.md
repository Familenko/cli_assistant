# Personal Assistant Chatbot CLI_ASSISTANT

Welcome to the Personal Assistant Chatbot, a Python-based command-line interface (CLI) application designed to manage your contacts and notes efficiently. This bot provides an easy way to store, search, edit, and delete contacts and notes, while also offering some advanced features like birthday reminders and tag-based sorting for notes.

# Project Overview
The main goal of this project was to create a system that allows users to interact with and manage records in a contact book and notes repository. The chatbot operates entirely via the CLI, enabling users to perform a variety of tasks related to contact and note management.

# Key Features
**1. Contact Management:**

- Store contacts with names, addresses, phone numbers, emails, and birthdays.
- Validate phone numbers and emails during the creation or editing of a contact.
- Search for contacts by various criteria (e.g., name).
- Edit and delete existing contacts.
- Display a list of contacts who have birthdays within a specified number of days from the current date.

**2. Note Management:**

- Add textual notes.
- Search, edit, and delete notes.
- Add tags (keywords) to notes for easy categorization and searching.
- Sort and filter notes based on tags.

**3. Data Persistence:**

- The assistant can be restarted without losing any data.

# Installation
**1. Prerequisites**
- Python 3.7 or later
  
**2. Setup**

To start working with the chatbot, clone the Repository:

```git clone https://github.com/yourusername/cli_assistant.git cd cli_assistant```

# Usage
To launch the chatbot, simply run the run.py script:

```python run.py```

The bot will guide you through the available commands. Below is a list of core commands you can use:

**Contact Management Commands:**
- *Add Contact:* Add a new contact with all necessary details.
- *Search Contact:* Search for contacts using various criteria like name.
- *Edit Contact:* Update the details of an existing contact.
- *Delete Contact:* Remove a contact from the contact book.
- *Upcoming Birthdays:* Display contacts with upcoming birthdays within a specified time frame.
- *Note Management Commands*
- *Add Note:* Create a new text note.
- *Search Notes:* Find notes based on content or tags.
- *Edit Note:* Modify an existing note.
- *Delete Note:* Remove a note.
- *Tag Note:* Add keywords to a note for better categorization.
- *Sort Notes by Tags:* Organize notes by their associated tags.

**Example Commands:**
- *Add a new contact:*
```add_contact "John Doe" "123 Main St" "+1234567890" "john@example.com" "1990-01-01"```

- *Search for a contact by name:*
```search_contact "John"```

- *List contacts with birthdays in the next 7 days:*
```upcoming_birthdays 7```

- *Add a new note with a tag:*
```add_note "Buy groceries" "#shopping"```

- *Search notes by tag:*
```search_notes "#shopping"```

# Contribution
Feel free to fork this project, make your changes, and submit a pull request. We welcome contributions that help improve the functionality and user experience.


