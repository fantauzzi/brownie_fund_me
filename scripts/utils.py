from brownie import MockV3Aggregator, network, accounts, config
from web3 import Web3


def is_local_network():
    current_net = network.show_active()
    return current_net in ('development', 'ganache-local', 'mainnet-fork-dev')

def is_forked_network():
    current_net = network.show_active()
    return current_net in ('mainnet-fork-dev')


def get_account():
    if is_local_network() or is_forked_network():
        return accounts[0]
    account = accounts.add(config['wallets']['from_key'])
    return account


def deploy_mock_price_feed(account):
    # If a moch price feed is already available on chain, use that instead of deploying a new one
    if len(MockV3Aggregator) >= 1:
        price_feed_address = MockV3Aggregator[-1]
    else:
        # If no mock price feed alrady on chain, then deploy one
        price_feed_address = MockV3Aggregator.deploy(
            8, Web3.toWei(2000, 'ether'), {'from': account})
    return price_feed_address
