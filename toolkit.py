import pickle
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import (
    has_completions,
    completion_is_selected,
)
from cli_assistant.ChatBot import ChatBot


# Override enter key to automatically perform first completion.

key_bindings = KeyBindings()
filter = has_completions & ~completion_is_selected
@key_bindings.add("enter", filter=filter)
def _(event):
    event.current_buffer.go_to_completion(0)
    event.current_buffer.validate_and_handle()

bot = ChatBot()

commands_dict = {"add": bot.add_contact,
                "add-notes": bot.add_notes
                      }

try:
    with open("cached.pickle", "rb") as fn:
        lst = pickle.load(fn)
except (EOFError, FileNotFoundError):
    lst = []

contacts = {}

while True:
    completer = FuzzyWordCompleter(lst)
    result = prompt("Enter command: ",
    # history="history.txt",
        completer=completer,
        complete_while_typing=True,
        key_bindings=key_bindings,
    )
    lst.append(result)
    command, *args = result
    if command in commands_dict:
        bot.commands_dict[command](args)
    #contacts[args[0]] = args[-1] if len(args)>1 else None #IndexError: list index out of range: contacts[args[0]] = args[-1] if len(args)>1 else None 
    with open("cached.pickle", "wb") as fn:
        pickle.dump(lst, fn)
    if result == 'q':
      #  print(contacts)
        break
