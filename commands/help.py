import os

#cargar comandos

def load_commands():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    commands_path = os.path.join(dir_path, 'help_files', 'commands.txt')
    try:
        with open(commands_path, 'r') as file:
            return {line.strip() for line in file if line.strip()}
    except FileNotFoundError:
        print("El archivo de comandos no se encontró.")
        return set()
    except Exception as e:
        print(f"Error al cargar la lista de comandos: {str(e)}")
        return set()

available_commands = load_commands()


def load_help(command, option):
    if command not in available_commands:
        return "El comando solicitado no existe."
    
    try:
        help_type = {'-d': 'd', '-m': 'm', '-s': 's'}.get(option, 'd')
        file_name = f"{command}_{help_type}.txt"
        dir_path = os.path.dirname(os.path.abspath(__file__))
        help_path = os.path.join(dir_path, 'help_files', file_name)
        with open(help_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "No hay ayuda disponible para el comando dado"
    except Exception as e:
        return str(e)

def execute_help(args):
    if len(args) == 0:
        # Ayuda general de cómo usar help
        return "Uso: help [opción] <comando>\nOpciones: -d, -m, -s"
    elif len(args) == 1:
        # Es una opción?
        # lo mismo que help -d <comando>
        return load_help(args[0], '-d')
    elif len(args) == 2:
        # El primero debe ser la opción, segundo es la instrucción
        if args[0] in ['-d', '-m', '-s']:
            return load_help(args[1], args[0])
        else:
            return "Formato de comando incorrecto, usa:\nhelp [opción] <comando>"
