from brownie import FundMe, MockV3Aggregator, config, network
from scripts.utils import get_account, deploy_mock_price_feed


def deploy_fund_me(account):
    current_net = network.show_active()
    publish_source = config['networks'][current_net]['verify']
    assert publish_source in (True, False)
    price_feed_address = config['networks'][current_net].get(
        'eth_usd_price_feed')
    if price_feed_address is None:
        price_feed_address = deploy_mock_price_feed(account)
        print(f'Using price feed deployed at {price_feed_address}')

    fund_me = FundMe.deploy(price_feed_address, {
                            'from': account}, publish_source=publish_source)
    return fund_me


def main():
    account = get_account()
    print(f'Working from account {account}')
    # If you print fund_me you get the deployed contract address
    fund_me = deploy_fund_me(account)
