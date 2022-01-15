import os
import sys

from brownie import *

from scripts.generadores import *
from scripts.visualizadores import *


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
                contract, voters, candidates = genVotantes(file_name, contract)
            
            elif base_command == 'genVotos':
                contract = genVotos(contract, voters, candidates, MIN_ABSTENTION, MAX_ABSTENTION)
            
            elif base_command == 'reportePorLocalidad':
                try:
                    index = int(tokenized_command[1])
                    print(reportePorLocalidad(contract, index))
                except:
                    index = 0
                    print(reportePorLocalidad(contract, index))

            # elif base_command == 'reporteTotal':
            #     print(reporteTotal(contract, candidates))

            elif base_command == 'reportePresidencial':
                print(reportePresidencial(contract))
                
            elif base_command == 'break':
                break
            
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
