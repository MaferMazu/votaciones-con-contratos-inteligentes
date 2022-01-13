import os
from pathlib import Path

from brownie import accounts

LOCATION = Path(__file__).absolute().parent.parent

def printSomething():
    print("something")

def genVotantes(file_name):
    """genVotantes."""
    try:
        with open(file_name, 'r') as f:
            print("Pude abrir")
            lines = f.readlines()
            for line in lines:
                try:
                    token = line.split(' ')
                    locality = token[0]
                    voters = int(token[1])
                    center = int(token[2])
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
                        print("Pude agregar")
                except:
                    print("No pude crear la cuenta.")
    except:
        print("No pude abrir el archivo.")
