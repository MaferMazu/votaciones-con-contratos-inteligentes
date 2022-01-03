import sys


def main():
    
    while True:
        try:
            command = input(">> ")
            tokenized_command = command.split(' ')
            base_command = tokenized_command[0]
            if base_command == 'genVotante':
                pass
            else:
                print("\nEl comando introducido no es válido.")
        except KeyboardInterrupt:
            print("\nHasta luego :D")
            sys.exit(0)

if __name__ == '__main__':
    main()
