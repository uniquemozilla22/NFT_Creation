


from brownie import UBNFT,config, network
from scripts. util import get_account



sample_token_uri = "https://ipfs.io/ipfs/QmdZffpu6b1fdcmyWwiAMZKFqGyBhURWtFLcksB1b9hqjN?filename=election.json"

def mint_additional():
    account = get_account()

    ubnft = UBNFT[-1]
    tx = ubnft.createLogoNFT(sample_token_uri,{"from": account})
    tx.wait(1)

def main():
    mint_additional()