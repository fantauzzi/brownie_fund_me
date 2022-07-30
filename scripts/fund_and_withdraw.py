from brownie import FundMe
from scripts.utils import get_account


def fund(account, fund_me, amount):
    fund_me.fund({'from': account, 'value': amount})


def withdraw(account, fund_me, amount):
    fund_me.withdraw({'from': account, 'value': amount})


def main():
    account = get_account()
    assert len(FundMe) >= 1
    fund_me = FundMe[-1]
    amount = fund_me.getEntranceFee()
    fund(account, fund_me, amount)
    withdraw(account, fund_me, amount)
