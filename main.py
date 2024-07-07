import os
import colorama
from colorama import Fore, Style
from commands.cd import change_directory
from commands.ls import list_directory
from commands.echo import print_message

colorama.init()

def clear_screen_before_execute():
    # Limpiar la pantalla antes de
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_command(command, current_path):
    parts = command.split()
    if parts:
        if parts[0] == 'cd':
            if len(parts) > 1:
                new_path = change_directory(parts[1])
                if new_path:
                    return new_path # devolver directorio.jsp
            else:
                print("cd command requires a path argument.")
        elif parts[0] == 'ls':
            list_directory()
        elif parts[0] == 'echo':
            print_message(' '.join(parts[1:]))
        else:
            print("Command not implemented.")
    return current_path  # Devolver directorio actual.js

def main():
    clear_screen_before_execute()  # Limpiar la pantalla al inicio
    print(Fore.CYAN + "Te damos la bienvenida a Shellbyville" + Style.RESET_ALL)
    current_path = os.getcwd() # dir actual
    while True:
        current_dir = os.path.basename(current_path) if current_path != '/' else '/'
        prompt = f"<{Fore.GREEN}Shellbyville:{Fore.BLUE}{current_dir}{Style.RESET_ALL}> "
        command = input(prompt)
        if command.lower() in ['exit', 'quit']:
            break
        current_path = execute_command(command, current_path)

if __name__ == "__main__":
    main()