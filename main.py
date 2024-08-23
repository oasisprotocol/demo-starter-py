from typing import Optional
from scripts.ContractUtility import ContractUtility
from scripts.utils import get_contract


def compile_contract(contract_name: str,
                     network_name: Optional[str] = "sapphire-localnet"
                     ) -> None:
    contract_utility = ContractUtility(network_name)
    contract_utility.setup_and_compile_contract(contract_name)

def deploy_contract(contract_name: str,
                    network_name: Optional[str] = "sapphire-localnet"
                    ) -> str:
    contract_utility = ContractUtility(network_name)
    contract_address = contract_utility.deploy_contract(contract_name)
    return contract_address

def set_message(contract_name: str,
                address: str,
                message:str,
                network_name: Optional[str] = "sapphire-localnet"
                ) -> None:
    contract_utility = ContractUtility(network_name)

    abi, bytecode = get_contract(contract_name)

    contract = contract_utility.w3.eth.contract(address=address, abi=abi)

    # Set a message
    tx_hash = contract.functions.setMessage(message).transact({'gasPrice': contract_utility.w3.eth.gas_price})
    tx_receipt = contract_utility.w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Message set. Transaction hash: {tx_receipt.transactionHash.hex()}")

def get_message(contract_name: str,
                address: str,
                network_name: Optional[str] = "sapphire-localnet"
                ) -> str:
    contract_utility = ContractUtility(network_name)

    abi, bytecode = get_contract(contract_name)

    contract = contract_utility.w3.eth.contract(address=address, abi=abi)
    # Retrieve message from contract
    message, author, sender = contract.functions.message().call()

    print(f"Retrieved message: {message}")
    print(f"Author: {author}")
    print(f"Sender: {sender}")

    return message

if __name__ == '__main__':
    contract_utility = ContractUtility()
    contract_utility.setup_and_compile_contract("MessageBox")
    contract_address = contract_utility.deploy_contract("MessageBox")
    set_message("MessageBox", contract_address)
    get_message("MessageBox", contract_address)