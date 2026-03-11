from web3 import Web3
import time

class SomniaExplorer:
    def __init__(self, rpc_url="https://rpc.shannon.somnia.network"):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        
    def check_connection(self):
        return self.w3.is_connected()

    def get_network_data(self):
        if not self.check_connection():
            return None
        
        latest_block = self.w3.eth.get_block('latest')
        gas_price = self.w3.eth.gas_price
        
        return {
            "block_height": latest_block['number'],
            "gas_gwei": self.w3.from_wei(gas_price, 'gwei'),
            "timestamp": latest_block['timestamp'],
            "tx_count": len(latest_block['transactions'])
        }

    def get_balance(self, address):
        try:
            checksum_address = self.w3.to_checksum_address(address)
            balance_wei = self.w3.eth.get_balance(checksum_address)
            return self.w3.from_wei(balance_wei, 'ether')
        except:
            return None