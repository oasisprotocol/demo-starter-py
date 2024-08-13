# config.py
import os

OASIS_RPC_URL = 'http://localhost:8545'
# OASIS_RPC_URL = 'https://testnet.sapphire.oasis.io'
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
SOLIDITY_VERSION = '0.8.0'

# Optional: Add error checking
if not all([OASIS_RPC_URL, PRIVATE_KEY]):
    raise Warning(
        "Missing required environment variables. Please set OASIS_RPC_URL, PRIVATE_KEY.")
