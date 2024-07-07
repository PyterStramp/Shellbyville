import os

def change_directory(path, flag, base_path, current_path):
    if not path:
        return None
    
    if path.startswith('/'):
        new_path = os.path.abspath(os.path.join(base_path, path.lstrip('/'))) # ruta absoluta para base_path
    else:
        new_path = os.path.abspath(os.path.join(current_path, path))
    if flag == '-P':
        new_path = os.path.realpath(new_path)  # enlace simbólico al path real

    if new_path.startswith(base_path):
        try:
            os.chdir(new_path)
            return os.getcwd()  # devuelve el nuevo directorio
        except OSError as e:
            print(f"Error cambiando directorio: {e}")
    else:
        print("El directorio está fuera de la base de Shellbyville")
    
    return None
