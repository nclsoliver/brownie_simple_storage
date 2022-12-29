from brownie import SimpleStorage, accounts, _config


def read_contract():
    print(SimpleStorage[0])



def main():
    read_contract()
