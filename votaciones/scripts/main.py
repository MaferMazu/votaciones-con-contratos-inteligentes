import os
import sys

from brownie import *

from scripts.generadores import *


def main():
    voters = []
    candidates = {}
    MIN_ABSTENTION = 10 #In %
    MAX_ABSTENTION = 30 #In %
    while True:
        try:
            command = input(">> ")
            tokenized_command = command.split(' ')
            base_command = tokenized_command[0]
            if base_command == 'genVotante':
                contract = accounts[0].deploy(Votaciones)
                file_name = str(tokenized_command[2])
                file_name = file_name.replace("'", "").replace('"', '')
                voters, candidates = genVotantes(file_name, contract)
            elif base_command == 'exit':
                print("\nHasta luego :D")
                sys.exit(0)
            elif base_command == 'accounts':
                print(accounts._accounts)
            else:
                print("\nEl comando introducido no es válido.")
        except KeyboardInterrupt:
            print("\nHasta luego :D")
            sys.exit(0)

if __name__ == '__main__':
    main()
