'''
Title of Project: Crypto
Autor: Matias Gonzalez
'''

# Imports
from time import time

from blockchain import Blockchain
from transaction import Transaction

# -------------------------------------------------------
# ------------------ TEST BLOCKCHAIN --------------------
# --------------------------------------------------------

my_crypto = Blockchain()

print("Matias began to mine...")

my_crypto.createTrans(Transaction("Agus", "Faby", 0.01))
my_crypto.createTrans(Transaction("Migue", "Arthur", 100))
my_crypto.createTrans(Transaction("Gaby", "Jude", 0.2))

start_time = time()
my_crypto.minePendingTrans("Matias")
final_time = time()
print(f"Matias delay: {final_time-start_time} secs")

print('-'*20)

print("Carlo began to mine...")

my_crypto.createTrans(Transaction("Fabio", "Faby", 1))
my_crypto.createTrans(Transaction("Maria", "Alba", 40))
my_crypto.createTrans(Transaction("Alba", "Joan", 2))

start_time = time()
my_crypto.minePendingTrans("Carlo")
final_time = time()
print(f"Carlo delay: {final_time-start_time} secs")

print('-'*20)

print("Pedro began to mine...")

my_crypto.createTrans(Transaction("Tomas", "Guille", 0.0001))
my_crypto.createTrans(Transaction("Marco", "Pedro", 4))
my_crypto.createTrans(Transaction("Soledad", "Laura", 20))

start_time = time()
my_crypto.minePendingTrans("Pedro")
final_time = time()
print(f"Pedro delay: {final_time-start_time} secs")

print('-'*20)
print("Matias have " +str(my_crypto.getBalance("Matias")) + " Jam3 in your Wallet")
print("Carlo have " +str(my_crypto.getBalance("Carlo")) + " Jam3 in your Wallet")
print("Pedro have " +str(my_crypto.getBalance("Pedro")) + " Jam3 in your Wallet")
print('-'*20)

# Chain block hash 
for x in range(len(my_crypto.chain)):
    print(f"Hash of Block {x}: {my_crypto.chain[x].hash}")

print(my_crypto.isChainValid())
