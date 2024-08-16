from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import (
    has_completions,
    completion_is_selected,
)
from ChatBot import ChatBot
from Tags import Tags


def main():
    key_bindings = KeyBindings()
    filter = has_completions & ~completion_is_selected
    @key_bindings.add("enter", filter=filter)
    def _(event):
        event.current_buffer.go_to_completion(0)
        event.current_buffer.validate_and_handle()

    bot = ChatBot()
    history = bot.history

    while True:
        completer = FuzzyWordCompleter(history)
        user_input = prompt("Enter command: ",
            completer=completer,
            complete_while_typing=True,
            key_bindings=key_bindings,
        )
        command, *args = user_input.lower().split() #to replace with parse_input() func
        if command == "search-notes":
            notes_search = input("Give me a tag to search for the note: ")
            if notes_search in Tags():
                print()

        if command in bot.commands:
            bot.commands[command](args)

        #TODO: add notes-search by tags/keywords
            
        if user_input == 'q':
            break
