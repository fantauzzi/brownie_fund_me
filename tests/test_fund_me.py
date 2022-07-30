from brownie import FundMe, MockV3Aggregator, accounts, config, network, exceptions
from scripts.utils import get_account, deploy_mock_price_feed, is_local_network
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me(account)
    amount = fund_me.getEntranceFee()
    tx = fund_me.fund({'from': account, 'value': amount})
    tx.wait(1)
    funded = fund_me.addressToAmountFunded(account)
    assert funded == amount
    tx2 = fund_me.withdraw({'from': account, 'value': amount})
    tx2.wait(1)
    funded2 = fund_me.addressToAmountFunded(account)
    assert funded2 == 0

def test_only_owner_can_withdraw():
    if not is_local_network():
        pytest.skip()
    not_owner = accounts[1]
    fund_me = FundMe[-1]
    amount = fund_me.getEntranceFee()
    with pytest.raises(exceptions.VirtualMachineError):
        tx = fund_me.withdraw({'from': not_owner, 'value': amount})

    
