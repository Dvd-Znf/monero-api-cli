from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession
from .version import __version__
from .rpc_methods import rpc_methods
from prompt_toolkit.styles import Style
from .functions import ip_address_validation
import re

style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    # Prompt.
    'prompt':           'ansicyan underline',
    'afterprompt':      '#ff0066 nounderline',
})

message = [
    ('class:prompt', 'cli mode'),
    ('class:afterprompt', ': '),
]

cli_completer = WordCompleter(['get_info', 'exit', 'version', 'help', 'daemon-address'])
session = PromptSession()

def cli(address, port):
    while True:
        try:
            user_input = session.prompt(message, style=style, completer=cli_completer) 
            
            if user_input == "exit":
                print("Exiting the CLI.")
                break
            elif user_input == "version":
                print(f"Version: {__version__}")
            elif ' ' in user_input and len((user_input.split(" "))) == 2 :
                first_arg, additional_arg = user_input.split(" ")
                if first_arg == "help":
                    rpc_methods[first_arg](address, port, additional_arg)
                elif first_arg == "daemon-address":
                    print(additional_arg)
                else:
                   print(first_arg + " is not known")
            elif user_input == "daemon-address":
                print("Please enter a valid daemon address")####
                
                daemon_address = input()

                address, port = ip_address_validation(daemon_address)

            elif user_input in rpc_methods:####
                rpc_methods[user_input](address, port)
            elif len(user_input) > 0 and not str.isspace(user_input):
                print(user_input + " is not known")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt. Exiting the CLI.")
            break
        except EOFError:
            print("\nEOF (Ctrl+D) detected. Exiting the CLI.")
            break
