from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import (
    has_completions,
    completion_is_selected,
)

from ChatBot import ChatBot


def input_hendler(user_input):
    try:
        command, *args = user_input.lower().split()
        return command, args
    except:
        return False, False


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
        user_input = prompt("Enter command or press 'q' to quit: ",
            completer=completer,
            complete_while_typing=True,
            key_bindings=key_bindings,
        )
        
        command, args = input_hendler(user_input)
        if not command:
            print("Invalid command")
            continue
        else:
            if command in bot.commands:
                try:
                    bot.commands[command](*args)
                except Exception as e:
                    print(e)
                    continue
            
                
            if user_input == 'q':
                bot.notebook.save_to_file()
                bot.book.save_to_file()
                break
