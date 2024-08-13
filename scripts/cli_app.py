#!/usr/bin/env python3

from ContractUtility import ContractUtility
from main import interact_with_contract
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
    compile_parser.add_argument('source', help="Source file or directory to compile")

    # Subparser for deploy
    deploy_parser = subparsers.add_parser('deploy', help="Deploy the smart contract")
    deploy_parser.add_argument('contract', help="Contract name or file to deploy")

    # Subparser for interact
    interact_parser = subparsers.add_parser('interact', help="Interact with a deployed contract")
    interact_parser.add_argument('name', help="Contract name to interact with")
    interact_parser.add_argument('address', help="Contract address to call")

    arguments = parser.parse_args()

    contract_utility = ContractUtility()

    if arguments.command == "compile":
        contract_utility.setup_and_compile_contract(arguments.source)

    elif arguments.command == "deploy":
        contract_utility.deploy_contract(arguments.contract)

    elif arguments.command == "interact":
        interact_with_contract(arguments.name, arguments.address)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
