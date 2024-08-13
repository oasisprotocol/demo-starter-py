import pytest
from ContractUtility import ContractUtility
from unittest.mock import MagicMock, patch


@patch('ContractUtility.Account.from_key', return_value='0xABCD')
@patch('ContractUtility.setup_web3_middleware', return_value={})
def test_contract_utility_init(mock_middleware, mock_account):
    util = ContractUtility()

    mock_middleware.assert_called_once()
    mock_account.assert_called_once()
    assert isinstance(util, ContractUtility)
    assert util.w3 == mock_middleware.return_value
    assert util.account == '0xABCD'


@patch('ContractUtility.compile_standard', return_value='compiled_sol')
@patch('ContractUtility.install_solc')
@patch('builtins.open', new_callable=MagicMock)
@patch('ContractUtility.Account.from_key', return_value='0xABCD')
@patch('ContractUtility.setup_web3_middleware', return_value={})
def test_setup_and_compile_contract(mock_middleware, mock_account, mock_open, mock_install_solc, mock_compile_standard):
    util = ContractUtility()
    contract_name = 'MessageBox'

    output = util.setup_and_compile_contract(contract_name)
    
    mock_install_solc.assert_called_once()
    mock_compile_standard.assert_called_once()

    assert output == 'compiled_sol'


@patch('ContractUtility.get_contract', return_value=('abi', 'bytecode'))
@patch('ContractUtility.Account.from_key', return_value='0xABCD')
@patch('ContractUtility.setup_web3_middleware', return_value={})
def test_deploy_contract(mock_middleware, mock_account, mock_get_contract):
    mock_eth = MagicMock()
    mock_eth.return_value = {'gasPrice': 'gas_price'}
    mock_w3 = MagicMock()
    mock_w3.eth = mock_eth
    contract_name = 'MessageBox'
    
    util = ContractUtility()
    util.w3 = mock_w3
   
    util.deploy_contract(contract_name)

    mock_middleware.assert_called_once()
    mock_account.assert_called_once()
    mock_get_contract.assert_called_once()
    assert mock_eth.contract.called