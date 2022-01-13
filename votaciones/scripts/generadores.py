import os
from pathlib import Path

from brownie import accounts
from faker import Faker

LOCATION = Path(__file__).absolute().parent.parent

def printSomething():
    print("something")

def genVotantes(file_name, contrato, direcciones):
    """genVotantes."""
    faker = Faker()
    localities = []
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                try:
                    token = line.rstrip("\n").split(' ')
                    locality = token[0]
                    voters = int(token[1])
                    center = int(token[2])
                    
                    # Create locality
                    contrato.registrarLocalidades([locality], {'from': accounts[0]})
                    localities.append(locality)

                    # Create votante
                    for i in range(voters):
                        name = f"{faker.first_name().lower()}"
                        email = f"{name}.{faker.last_name().lower()}@{faker.domain_name()}"
                        data = {
                            "name": name,
                            "email": email,
                            "locality": locality,
                            "center": i%center
                        }
                        address = accounts.add()
                        direcciones[address] = data
                        index = int(len(localities)-1)

                        contract.registrarVotante(address, name, email, index, {'from': accounts[0]})
                except:
                    print("No pude crear la cuenta.")
    except:
        print("No pude abrir el archivo.")
