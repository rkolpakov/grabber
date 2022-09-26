import json
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/72jiNsaKYgLmrpborA97DR2oNn0Pf7fs"))

with open("abi/erc20.json") as f:
    abi = json.load(f)

with open("contracts.txt", "r") as f:
    contracts = f.read().splitlines()

with open("holders.txt", "r") as f:
    holders = f.read().splitlines()


result = {}

for holder in holders:
    balances = []

    for contract_address in contracts:
        c = w3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=abi)
        balance = c.functions.balanceOf(Web3.toChecksumAddress(holder)).call()

        if (balance > 0):
            obj = {}
            obj[contract_address] = balance
            balances.append(obj)

    result[holder] = balances

with open('result.json', 'w') as f:
    json.dump(result, f)
