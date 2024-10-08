import os

# Set default private key
if os.environ.get("PRIVATE_KEY") is None:
    os.environ["PRIVATE_KEY"] = (
        "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"
    )

from src.MessageBox import set_message, get_message
from src.ContractUtility import ContractUtility
from unittest.mock import MagicMock, patch


@patch("src.ContractUtility.setup_web3_middleware", return_value=MagicMock())
def test_contract_utility_init(mock_middleware):
    util = ContractUtility("sapphire-localnet")

    mock_middleware.assert_called_once()
    assert isinstance(util, ContractUtility)
    assert util.w3 == mock_middleware.return_value


@patch("src.ContractUtility.compile_standard", return_value="compiled_sol")
@patch("src.ContractUtility.install_solc")
@patch("builtins.open", new_callable=MagicMock)
@patch("src.ContractUtility.setup_web3_middleware", return_value={})
def test_setup_and_compile_contract(
    mock_middleware, mock_open, mock_install_solc, mock_compile_standard
):
    util = ContractUtility("sapphire-localnet")
    contract_name = "MessageBox"

    output = util.setup_and_compile_contract(contract_name)

    mock_install_solc.assert_called_once()
    mock_compile_standard.assert_called_once()

    assert output == "compiled_sol"


@patch("src.ContractUtility.get_contract", return_value=("abi", "bytecode"))
@patch("src.ContractUtility.setup_web3_middleware", return_value={})
def test_deploy_contract(mock_middleware, mock_get_contract):
    mock_eth = MagicMock()
    mock_eth.return_value = {"gasPrice": "gas_price"}
    mock_w3 = MagicMock()
    mock_w3.eth = mock_eth
    contract_name = "MessageBox"

    util = ContractUtility("sapphire-localnet")
    util.w3 = mock_w3

    util.deploy_contract(contract_name)

    mock_middleware.assert_called_once()
    mock_get_contract.assert_called_once()
    assert mock_eth.contract.called


def test_compiles_contract_successfully():
    """
    Make sure sapphire-localnet is running before running the following tests!
    """
    contract_utility = ContractUtility("sapphire-localnet")
    contract_name = "MessageBox"
    contract_utility.setup_and_compile_contract(contract_name)
    assert contract_name + "_compiled.json" in os.listdir("compiled_contracts/")


def test_deploys_contract_successfully():
    contract_name = "MessageBox"
    contract_utility = ContractUtility("sapphire-localnet")
    contract_address = contract_utility.deploy_contract(contract_name)
    assert contract_utility.w3.eth.get_code(contract_address) != "0x"


def test_sets_message_successfully():
    contract_name = "MessageBox"
    contract_message = "Hello World"
    contract_utility = ContractUtility("sapphire-localnet")
    contract_address = contract_utility.deploy_contract(contract_name)
    set_message(contract_address, contract_message)
    assert get_message(contract_address) == contract_message
