import os
import random

from brownie import accounts
from faker import Faker

from scripts.models import Candidato, Votante


def genVotantes(file_name, contract):
    """genVotantes."""
    faker = Faker()
    voters_list = []
    candidates = {"All":[]}
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            index_localion = 0
            index_candidate = 1
            for line in lines:
                token = line.rstrip("\n").split(' ')
                locality = token[0]
                voters = int(token[1])
                center = int(token[2])
                
                # Create locality
                contract.registrarLocalidades([locality], {'from': accounts[0]})
                candidates[locality]=[]

                # Create votante
                index_first_voter_in_this_locality = len(voters_list)
                for i in range(voters):
                    name = f"{faker.first_name().lower()}"
                    email = f"{name}.{faker.last_name().lower()}@{faker.domain_name()}"
                    address = accounts.add()
                    data=Votante(address, name, email, locality, i%center)
                    voters_list.append(data)
                    
                    # Register in contract
                    contract.registrarVotante(address, name, email, index_localion, {'from': accounts[0]})

                    # Transfer 10.000.000 weis
                    accounts[1].transfer(address, "10000000 wei")
                
                # Create candidates
                base = int(voters*0.01)
                base = base if base>0 else 2
                top = int(voters/4)
                top = top if top>2 else 3
                how_much_candidates = random.choice(range(base, top))

                selected_candidates = random.sample(voters_list[index_first_voter_in_this_locality:], how_much_candidates+1)
                
                for elem in selected_candidates[1:]:
                    contract.registrarCandidato(elem.address, False, {'from': accounts[0]})
                    candidate = Candidato(elem, index_candidate)
                    candidates[locality].append(candidate)
                    index_candidate += 1

                contract.registrarCandidato(selected_candidates[0].address, True, {'from': accounts[0]})
                candidates["All"].append(candidate)
                index_candidate += 1

                index_localion+=1        
    except:
        print("No se pudo abrir el archivo.")

    return voters_list, candidates


def genVotos(voters, candidates):
    """genVotos."""
