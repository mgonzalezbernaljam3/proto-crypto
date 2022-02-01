'''
Title of Project: Crypto
Autor: Matias Gonzalez
'''


class Transaction:
    def __init__(self, fromWallet, toWallet, amount):
        self.fromWallet = fromWallet
        self.toWallet = toWallet
        self.amount = amount
