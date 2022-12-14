from brownie import accounts, config, SimpleStorage, network

# from brownie.network import gas_price
# from brownie.network.gas.strategies import LinearScalingStrategy
# gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
# gas_price(gas_strategy)


def deploy_simple_storage():
    # account = accounts.loafd("whatever name you want")
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # simple_storage.wait(1)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
