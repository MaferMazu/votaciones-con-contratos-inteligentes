from brownie import accounts

def reportePorLocalidad(contract, index):
    locality, name, num_votos, abstention = contract.reportePorLocalidad(index, {'from': accounts[0]})
    return f"== {locality} ==\nGobernador más votado: {name}\nNumero de votos: {num_votos}\nAbstención: {abstention}%\n"

def reportePresidencial(contract):
    locality, name, num_votos, abstention = contract.reportePresidencial({'from': accounts[0]})
    return f"== {locality} ==\nPresidente más votado: {name}\nNumero de votos: {num_votos}\nAbstención: {abstention}%\n"

# def reporteTotal(contract, candidates):
#     resp = reportePresidencial(contract) + '\n'
#     for index in range(len(candidates)):
#         resp = resp + reportePorLocalidad(contract, index)
#     return resp
