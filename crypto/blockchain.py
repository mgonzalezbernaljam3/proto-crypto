'''
Title of Project: Crypto
Autor: Matias Gonzalez
'''

import datetime
import json
import pprint

from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 5 
        self.pendingTransaction = []
        self.reward = 3

    def createGenesisBlock(self):
        # Link to access Block 0 of BTC: # https://www.blockchain.com/btc/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
        genesisBlock = Block(str(datetime.datetime.now()), "I'm the 0 of the blockchain")
        return genesisBlock

    def getLastBlock(self):
        return self.chain[len(self.chain)-1]

    def minePendingTrans(self, minerRewardAddress):
        newBlock = Block(str(datetime.datetime.now()), self.pendingTransaction)
        newBlock.mineBlock(self.difficulty)
        newBlock.previousBlock = self.getLastBlock().hash

        print(f"Hash of previous block: {newBlock.previousBlock}")
        
        testChain = []
        for trans in newBlock.trans:
            temp = json.dumps(trans.__dict__, indent=5, separators=(',',':'))
            testChain.append(temp)
        pprint.pprint(testChain)

        self.chain.append(newBlock)
        print(f"Hash of Block: {newBlock.hash}")
        print("¡New block added!")

        rewardTrans = Transaction("System" , minerRewardAddress, self.reward)
        self.pendingTransaction.append(rewardTrans)
        self.pendingTransaction = []

    def isChainValid(self):
        for x in range(1, len(self.chain)):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]

            if (currentBlock.previousBlock != previousBlock.hash):
                print("The chain is invalid!")
        
        print("The chain is valid and safe!")

    def createTrans(self, transaction):
        self.pendingTransaction.append(transaction)

    def getBalance(self, walletAddress):
        balance = 0
        for block in self.chain:
            if block.previousBlock == "":
                continue
            for transaction in block.trans:
                if transaction.fromWallet == walletAddress:
                    balance -= transaction.amount
                if transaction.toWallet == walletAddress:
                    balance += transaction.amount
        return balance
