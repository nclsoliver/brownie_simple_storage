from brownie import SimpleStorage, accounts, _config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # go take the index thats one less than the length
    # ABI
    # Add
    print(simple_storage.retrieve())



def main():
    read_contract()
