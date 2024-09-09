from typing import Optional
from src.ContractUtility import ContractUtility
from src.utils import get_contract


def set_message(address: str,
                message:str,
                network_name: Optional[str] = "sapphire-localnet"
                ) -> None:
    contract_utility = ContractUtility(network_name)

    abi, bytecode = get_contract('MessageBox')

    contract = contract_utility.w3.eth.contract(address=address, abi=abi)

    # Set a message
    tx_hash = contract.functions.setMessage(message).transact({'gasPrice': contract_utility.w3.eth.gas_price})
    tx_receipt = contract_utility.w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Message set. Transaction hash: {tx_receipt.transactionHash.hex()}")

def get_message(address: str,
                network_name: Optional[str] = "sapphire-localnet"
                ) -> str:
    contract_utility = ContractUtility(network_name)

    abi, bytecode = get_contract('MessageBox')

    contract = contract_utility.w3.eth.contract(address=address, abi=abi)
    # Retrieve message from contract
    message = contract.functions.message().call()
    author = contract.functions.author().call()

    print(f"Retrieved message: {message}")
    print(f"Author: {author}")

    return message
