from faker import Faker
from models.accounts import VoterAccounts

faker = Faker()

def voter_generator(self, file):
    """Voter Generator."""
    voter_accounts = VoterAccounts()
    with open(file, 'r') as f:
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
                    VoterAccounts.add(data)
            except:
                pass
    return voter_accounts
