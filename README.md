# Oasis Starter dApp in Python

This is a skeleton for confidential Oasis dApps in Python.

## Prerequisites

This project was tested on python 3.10, but should work with most python3 versions. 
Use pyenv to handle multiple python installations.

1. Create the environment using venv (or pipx) ```python3 -m venv my_env``` and install the python sapphire wrapper. The library is currently **NOT** included in the PyPI repository so make sure to only install the local .whl version.

2. Make sure to follow the [instructions](https://github.com/oasisprotocol/sapphire-paratime/tree/main/clients/py "Py client wrapper") and build the .whl file correctly. Install the wheel.

3. Install the packages in requirements.txt ```pip install -r requirements.txt```

## Setup

1. Include the RPC url in the **scripts/config.py**. If running sapphire-localnet make sure to launch the [local node](https://github.com/oasisprotocol/oasis-web3-gateway/tree/main/docker).
2. Add your deployer private key to the environment variables ```export PRIVATE_KEY=<my_private_key>```.


## Testing

Some inital unit tests are located in **./test** folder. Run ```pytest``` in the terminal. 

## Running

The **./scripts** folder contains the .py files which are used to compile, deploy and interact with the contracts inside **./contracts** folder.
It also contains the ```cli_app.py``` for command line development. Again make sure to follow the setup [instructions](#Setup) before running scripts.
Open main.py which contains a simple starter example.

### Compiling the contract

After saving the .sol contract in **./contracts** folder, we can continue with compilation step. 

To compile:
```python
from scripts.ContractUtility import ContractUtility
contract_utility = ContractUtility()
contract_utility.setup_and_compile_contract("MessageBox")
```

### Deploying the contract

```python
contract_utility.deploy_contract("MessageBox")
```
Provide the contract name, in the starter example case we use the provided **MessageBox** without the .sol extension.

### Interacting with the contract

To help you get started with development,  ```main.py``` contains some functionality that showcases web3.py contract abstraction interaction.
It contains ```set_message()``` and ```get_message()``` functions that set message and query the contract view function ```message()``` respectively.


### Run example
To run: ```python3 main.py```

### CLI development
To compile, deploy and call the interact_with_contract() function from the terminal:
```shell
python cli_app.py compile --contract MessageBox
python3 python cli_app.py deploy --contract MessageBox --network sapphire-localnet
python3 cli_app.py set_message --name MessageBox --address <contract_address> --message "Hello world" --network sapphire-localnet
python3 cli_app.py get_message --name MessageBox --address <contract_address> --network  sapphire-localnet
```
