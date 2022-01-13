import os
import sys

from brownie import *
from faker import Faker

from scripts.generators import *


def main():
    print(os.getcwd())
    print(os.system('ls'))
    contrato = accounts[0].deploy(Votaciones)
    my_accounts = []
    while True:
        try:
            command = input(">> ")
            tokenized_command = command.split(' ')
            base_command = tokenized_command[0]
            if base_command == 'genVotante':
                file_name = str(tokenized_command[2])
                file_name = file_name.replace("'", "").replace('"', '')
                genVotantes(file_name)
            elif base_command == 'print':
                printSomething()
            elif base_command == 'exit':
                print("\nHasta luego :D")
                sys.exit(0)
            elif base_command == 'accounts':
                print(repr(accounts))
            else:
                print("\nEl comando introducido no es válido.")
        except KeyboardInterrupt:
            print("\nHasta luego :D")
            sys.exit(0)

if __name__ == '__main__':
    main()
