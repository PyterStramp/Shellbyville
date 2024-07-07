def main():
    while True:
        command = input("<Shellbyville> ")
        if command == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command == "help":
            print("Comandos disponibles: echo, help, exit")
        else:
            print("Comando no soportado flaco")

if __name__ == "__main__":
    main()
