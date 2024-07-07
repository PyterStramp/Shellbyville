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

def execute_command(command, current_path, base_path):
    parts = command.split()
    if parts:
        if parts[0] == 'cd':
            flag = '-L'  # Config por default
            path = None
            
            if len(parts) > 1:
                if parts[1] in ['-L', '-P']:
                    flag = parts[1]
                    if len(parts) > 2:
                        path = parts[2]
                    else:
                        print("El comando CD requiere el modificador -L o -P ")
                        return current_path
                else:
                    path = parts[1]
                
                new_path = change_directory(path, flag, base_path, current_path)
                if new_path:
                    return new_path  # devolver el nuevo directorio
            else:
                print("Se requiere una dirección antes de cambiar directorio")
                
        elif parts[0] == 'ls':
            list_directory()
        elif parts[0] == 'echo':
            print_message(' '.join(parts[1:]))
        else:
            print("Comando no implementado/reconocido.")
    return current_path  # devolver el directorio actual

def main():
    clear_screen_before_execute()  # Limpiar la pantalla al inicio

    base_path = os.path.abspath(os.getcwd())
    current_path = base_path  # dir base de Shellbyville
    print(Fore.CYAN + "Esperando órdenes" + Style.RESET_ALL)

    while True:
        relative_path = os.path.relpath(current_path, base_path)
        prompt = f"{Fore.GREEN}<Shellbyville:{Fore.BLUE}{relative_path if relative_path != '.' else ''}{Style.RESET_ALL}> "
        command = input(prompt)
        if command.lower() in ['exit', 'quit']:
            print(Fore.CYAN + "Nos hemos ido" + Style.RESET_ALL)
            break
        current_path = execute_command(command, current_path, base_path)

if __name__ == "__main__":
    main()