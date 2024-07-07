import subprocess
import os

def execute_command(command):
    try:
        if command.startswith('cd '):
            os.chdir(command.split(' ')[1])
        else:
            subprocess.run(command, check=True, shell=True)
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        command = input("Shellbyville> ")
        if command.lower() in ['exit', 'quit']:
            break
        execute_command(command)

if __name__ == "__main__":
    main()
