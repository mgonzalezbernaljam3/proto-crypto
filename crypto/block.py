'''
Title of Project: Crypto
Autor: Matias Gonzalez
'''

import hashlib


class Block:
    def __init__(self, timeStamp, trans, previousBlock = ''):
        self.timeStamp = timeStamp
        self.trans = trans
        self.previousBlock = previousBlock
        self.difficultyIncrement = 0
        self.hash = self.calculateHash(trans, timeStamp, self.difficultyIncrement)

    # Function to calculate the hash
    def calculateHash(self, data, timeStamp, difficultyIncrement):
        data = str(data) + str(timeStamp) + str(difficultyIncrement)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()

    # Block mining function
    def mineBlock(self, difficulty):
        # Hash : 00000...004faqft62...
        difficultyCheck = "0" * difficulty
        # 00000004faqft62szvyqvy7262...
        while self.hash[:difficulty] != difficultyCheck:
            self.hash = self.calculateHash(self.trans, self.timeStamp, self.difficultyIncrement)
            self.difficultyIncrement += 1
