


from brownie import UBNFT,  config, network
from scripts. util import get_account



sample_token_uri = "https://ipfs.io/ipfs/QmVYjy5hEWWFEYpCaFFExMajE1WZ9XaUgAiqF3jvWm5oWD?filename=yogesh.json"

def deploy_and_mint_one():
    account = get_account()

    ubnft = UBNFT.deploy({"from": account},publish_source=config["networks"][network.show_active()].get("verify"))
    tx = ubnft.createLogoNFT(sample_token_uri,{"from": account})
    tx.wait(1)

def main():
    deploy_and_mint_one()