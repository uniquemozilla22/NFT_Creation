

from brownie import UBNFT,  config, network
from scripts.util import get_account
from scripts.metadata import create_metadata

simple_token_uri = "https://ipfs.io/ipfs/{}?filename={}"



def deploy_and_mint_all():
    account = get_account()
    
    ubnft =  UBNFT.deploy({"from": account},publish_source=config["networks"][network.show_active()].get("verify"))
    
    metadatas = create_metadata()
    
    for metadata in metadatas:
        token_uri =  simple_token_uri.format(metadata["CID"],metadata["filename"])
        tx = ubnft.createLogoNFT(token_uri,{"from":account})
        tx.wait(1)
        

def main():
    deploy_and_mint_all()