import os

def list_directory():
    try:
        entries = os.listdir('.')
        for entry in entries:
            print(entry)
    except OSError as e:
        print(f"Error listando directorio: {e}")
