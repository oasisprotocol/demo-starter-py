from ContractUtility import ContractUtility
from utils import get_contract


def interact_with_contract(contract_name, contract_address):
    contract_utility = ContractUtility()

    abi, bytecode = get_contract(contract_name)

    contract = contract_utility.w3.eth.contract(address=contract_address, abi=abi)

    # Set a message
    tx_hash = contract.functions.setMessage("Hello, Oasis!").transact({'gasPrice': contract_utility.w3.eth.gas_price})
    tx_receipt = contract_utility.w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Message set. Transaction hash: {tx_receipt.transactionHash.hex()}")

    # Retrieve message from contract
    message, author, sender = contract.functions.message().call()

    print(f"Retrieved message: {message}")
    print(f"Author: {author}")
    print(f"Sender: {sender}")

if __name__ == '__main__':
    contract_utility = ContractUtility()
    contract_utility.setup_and_compile_contract("MessageBox")
    contract_address = contract_utility.deploy_contract("MessageBox")
    interact_with_contract("MessageBox", contract_address)