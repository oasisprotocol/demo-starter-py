#!/usr/bin/env python3

from scripts.ContractUtility import ContractUtility
from main import set_message, get_message
import argparse

def main():
    """
    Main method for the Python CLI tool.

    :return: None
    """
    parser = argparse.ArgumentParser(description="A Python CLI tool for compiling, deploying, and interacting with smart contracts.")

    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    # Subparser for compile
    compile_parser = subparsers.add_parser('compile', help="Compile the source code")
    compile_parser.add_argument('--contract', help="Name of the contract to compile", required=True)


    # Subparser for deploy
    deploy_parser = subparsers.add_parser('deploy', help="Deploy the smart contract")
    deploy_parser.add_argument('--contract', help="Name of the contract to deploy", required=True)
    deploy_parser.add_argument('--network', help="Chain name to connect to "
                                               "(sapphire, sapphire-testnet, sapphire-localnet)", required=True)

    # Subparser for set message
    setter_parser = subparsers.add_parser('setMessage', help="Interact with a deployed contract")
    setter_parser.add_argument('--name', help="Contract name to interact with", required=True)
    setter_parser.add_argument('--address', help="Contract address to call", required=True)
    setter_parser.add_argument('--message', help="Message to store in the contract", required=True)
    setter_parser.add_argument('--network', help="Chain name to connect to "
                                               "(sapphire, sapphire-testnet, sapphire-localnet)", required=True)

    # Subparser for get message
    getter_parser = subparsers.add_parser('message', help="Interact with a deployed contract")
    getter_parser.add_argument('--name', help="Contract name to interact with", required=True)
    getter_parser.add_argument('--address', help="Contract address to call", required=True)
    getter_parser.add_argument('--network', help="Chain name to connect to "
                                               "(sapphire, sapphire-testnet, sapphire-localnet)", required=True)

    arguments = parser.parse_args()


    if arguments.command == "compile":
        contract_utility = ContractUtility('sapphire-localnet')
        contract_utility.setup_and_compile_contract(arguments.contract)

    elif arguments.command == "deploy":
        contract_utility = ContractUtility(arguments.network)
        contract_utility.deploy_contract(arguments.contract)

    elif arguments.command == "setMessage":
        set_message(arguments.name, arguments.address, arguments.message, arguments.network)

    elif arguments.command == "message":
        get_message(arguments.name, arguments.address, arguments.network)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
