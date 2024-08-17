import colorama
from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import (
    has_completions,
    completion_is_selected,
)

from ChatBot import ChatBot

colorama.init(autoreset=True)

def input_hendler(user_input):
    try:
        command, *args = user_input.split()
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
        message = "Enter command or press 'q' to quit: "
        user_input = prompt(message,
            completer=completer,
            complete_while_typing=True,
            key_bindings=key_bindings,
        )

        if user_input == 'q':
            bot.save_data()
            break
        
        command, args = input_hendler(user_input)
        if not command or command not in bot.commands:
            print(Fore.RED + "Invalid command")
            continue
        else:
            if command in bot.commands:
                try:
                    bot.commands[command](*args)
                except Exception as e:
                    print(Fore.RED + f"Error: {e}")
                    continue
