import os

def change_directory(path):
    try:
        os.chdir(path)
        return os.getcwd()  # Devuelve el nuevo directorio de trabajo actual
    except OSError as e:
        print(f"Error cambiando directorio: {e}")
        return None
